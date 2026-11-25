import json
import os
from pathlib import Path
from datetime import datetime
import requests
from django.shortcuts import render

BMKG_URL = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json"
CACHE_PATH = Path(__file__).resolve().parent / "data" / "gempaterkini.json"

def fetch_gempa_data():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    data = None
    try:
        response = requests.get(BMKG_URL, headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            # Perbarui cache lokal
            os.makedirs(CACHE_PATH.parent, exist_ok=True)
            with open(CACHE_PATH, 'w', encoding='utf-8') as f:
                f.write(response.text)
    except Exception:
        pass

    # Jika request gagal (misal koneksi offline), gunakan data cache lokal
    if not data and CACHE_PATH.exists():
        with open(CACHE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)

    return data

def gempaterkini(request):
    raw_data = fetch_gempa_data()
    gempa_list = []
    waktu_update = datetime.now().strftime("%H:%M:%S")

    if raw_data and 'Infogempa' in raw_data and 'gempa' in raw_data['Infogempa']:
        items = raw_data['Infogempa']['gempa'][:15]
        for idx, item in enumerate(items, 1):
            coord_str = item.get('Coordinates', '')
            lat = 0.0
            lng = 0.0
            if coord_str:
                parts = coord_str.split(',')
                try:
                    lat = float(parts[0].strip())
                    lng = float(parts[1].strip())
                except ValueError:
                    pass

            kedalaman_str = item.get('Kedalaman', '')
            kedalaman_val = 0
            try:
                kedalaman_val = int(kedalaman_str.replace('km', '').strip())
            except ValueError:
                pass

            # Klasifikasi kedalaman BMKG:
            # Dangkal: < 70 km (Merah)
            # Menengah: 70 - 300 km (Oranye)
            # Dalam: > 300 km (Hijau)
            if kedalaman_val < 70:
                kategori = "Dangkal"
                color = "#dc2626"
            elif kedalaman_val <= 300:
                kategori = "Menengah"
                color = "#ea580c"
            else:
                kategori = "Dalam"
                color = "#16a34a"

            try:
                mag = float(item.get('Magnitude', 5.0))
            except ValueError:
                mag = 5.0

            gempa_list.append({
                'no': idx,
                'tanggal': item.get('Tanggal', ''),
                'jam': item.get('Jam', ''),
                'datetime': item.get('DateTime', ''),
                'lat': lat,
                'lng': lng,
                'lintang': item.get('Lintang', ''),
                'bujur': item.get('Bujur', ''),
                'magnitude': item.get('Magnitude', ''),
                'magnitude_val': mag,
                'kedalaman': item.get('Kedalaman', ''),
                'kedalaman_val': kedalaman_val,
                'wilayah': item.get('Wilayah', ''),
                'potensi': item.get('Potensi', ''),
                'kategori': kategori,
                'color': color,
            })

    context = {
        'gempa_list': gempa_list,
        'gempa_json': json.dumps(gempa_list),
        'total': len(gempa_list),
        'waktu_update': waktu_update,
    }
    return render(request, 'gempabumi/gempaterkini.html', context)
