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
    │   ├── settings.py              <-- Pengaturan INSTALLED_APPS & Referrer Policy
    │   ├── urls.py                  <-- Routing URL utama
    │   ├── wsgi.py
    │   └── asgi.py
    │
    ├── petaindonesia/               <-- Modul Peta Indonesia & Jabodetabek
    │   ├── views.py                 <-- View welcome & menu utama
    │   ├── view_peta.py             <-- View petasatu & petadua
    │   ├── urls.py                  <-- Routing URL modul petaindonesia
    │   └── templates/
    │       └── petaindonesia/
    │           ├── index.html       <-- Halaman menu utama
    │           ├── petasatu.html    <-- Peta Indonesia (Leaflet.js)
    │           └── petadua.html     <-- Peta Jabodetabek dengan kontrol pilih kota
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
