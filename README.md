# Proyek WebGIS Django (`webumkm`)

Tugas praktikum Sistem Informasi Geografis (SIG) berbasis Python Django Framework dan pustaka peta Leaflet.js.

---

## 📂 Struktur Direktori Proyek

```
Project web GIS/
│
├── run.bat                          <-- Skrip batch untuk menjalankan server
├── README.md                        <-- Dokumentasi proyek
│
└── webumkm/                         <-- Direktori Root Project Django
    ├── db.sqlite3
    ├── manage.py
    │
    ├── webumkm/                     <-- Konfigurasi Utama Django
    │   ├── settings.py              <-- Pengaturan INSTALLED_APPS, STATICFILES_DIRS, Referrer Policy
    │   ├── urls.py                  <-- Routing URL utama
    │   ├── wsgi.py
    │   └── asgi.py
    │
    ├── static/                      <-- Direktori File Statis & Data Spasial
    │   └── json/
    │       ├── provinces.json       <-- Data koordinat 34 provinsi se-Indonesia
    │       ├── 31.geojson           <-- Polygon DKI Jakarta
    │       ├── 32.geojson           <-- Polygon Jawa Barat
    │       ├── 33.geojson           <-- Polygon Jawa Tengah
    │       ├── 34.geojson           <-- Polygon DI Yogyakarta
    │       ├── 35.geojson           <-- Polygon Jawa Timur
    │       ├── 36.geojson           <-- Polygon Banten
    │       ├── profil_petani_jawa.csv <-- Data mentah CSV BPS 2024
    │       └── petani_jawa.json     <-- Hasil konversi JSON data non-spasial pertanian Jawa
    │
    ├── petaindonesia/               <-- Modul Peta Indonesia, Jabodetabek, Provinsi & Jawa
    │   ├── views.py                 <-- View welcome & menu utama
    │   ├── view_peta.py             <-- View petasatu, petadua, peta_provinsi, petani_jawa
    │   ├── urls.py                  <-- Routing URL modul petaindonesia
    │   └── templates/
    │       └── petaindonesia/
    │           ├── index.html       <-- Halaman menu utama
    │           ├── petasatu.html    <-- Peta Indonesia (Leaflet.js)
    │           ├── petadua.html     <-- Peta Jabodetabek dengan kontrol pilih kota
    │           ├── peta_provinsi.html <-- Peta 34 provinsi dari file provinces.json
    │           └── petani_jawa.html <-- Peta tematik choropleth polygon 6 provinsi Pulau Jawa
    │
    └── gempabumi/                   <-- Modul Gempa Terkini BMKG
        ├── views.py                 <-- Mengambil & mengolah data JSON BMKG
        ├── urls.py                  <-- Routing URL modul gempabumi
        ├── data/
        │   └── gempaterkini.json    <-- Backup data lokal BMKG
        └── templates/
            └── gempabumi/
                └── gempaterkini.html <-- Tampilan peta gempa interaktif & sidebar
```

---

## 🚀 Cara Menjalankan Server

### Opsi 1: Lewat Terminal (Command Prompt / PowerShell)
```bash
cd webumkm
python manage.py runserver
```

### Opsi 2: Menggunakan `run.bat`
Klik ganda file `run.bat` pada direktori ini.

---

## 🌐 Daftar URL Halaman

- **Menu Utama**: [http://localhost:8000/](http://localhost:8000/)
- **Halaman Welcome**: [http://localhost:8000/welcome/](http://localhost:8000/welcome/)
- **Peta Indonesia**: [http://localhost:8000/petasatu/](http://localhost:8000/petasatu/)
- **Peta Jabodetabek**: [http://localhost:8000/petadua/](http://localhost:8000/petadua/)
- **Peta Gempa BMKG**: [http://localhost:8000/gempabumi/](http://localhost:8000/gempabumi/)
- **Peta Provinsi Indonesia (JSON Spasial)**: [http://localhost:8000/petaindonesia/provinsi/](http://localhost:8000/petaindonesia/provinsi/)
- **Peta Sebaran Petani & Lahan Pertanian Jawa (GeoJSON Polygon + Data Non Spasial)**: [http://localhost:8000/petaindonesia/petani_jawa/](http://localhost:8000/petaindonesia/petani_jawa/)
