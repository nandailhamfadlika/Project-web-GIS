@echo off
title Menjalankan WebGIS Django - webumkm
echo ===================================================
echo   Menjalankan Server WebGIS Django (webumkm)
echo ===================================================
echo.
cd webumkm
echo Buka browser pada alamat:
echo http://localhost:8000/
echo.
python manage.py runserver 8000
pause
