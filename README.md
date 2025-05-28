# cmorph_downloader
Using Python and curl to download 30-minute CMORPH data with 8x8km spatial resolution

Repositori ini berisi skrip dan panduan untuk mengunduh data curah hujan satelit dari produk **CMORPH (Climate Prediction Center Morphing Technique)** 30menit dengan resolusi spasial 8x8km.

## 📌 Deskripsi

[CMORPH] (https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/30min/8km/) adalah produk curah hujan satelit global yang dikembangkan oleh NOAA. Dataset ini memiliki resolusi spasial tinggi dan cocok untuk berbagai aplikasi seperti klimatologi, analisis curah hujan ekstrem, serta pemodelan kekeringan dan banjir. 

## 🗂️ Struktur Repositori
- `list_data_cmorph.py`
 Skrip Python untuk membuat list url data cmorph yang dibagi menjadi 4 files .txt. Dapat diubah untuk pertahun atau sepanjang tahun yang diinginkan

- `download_cmorph_multi.bat` dan `download_cmorph_single.bat`
 Merupakan windows batch file yang digunakan untuk mendownload data berdasarkan files .txt yang ada

- `README.md` – Dokumentasi repositori ini

## 📥 Cara Menggunakan

1. Buatlah list data dari tahun yang ingin di download menggunakna `list_data_cmorph.py`.
2. Letakkan pada sebuah folder, lalu copy files `download_cmorph_multi.bat` dan `download_cmorph_single.bat`.
3. Double click pada file `download_cmorph_multi.bat` untuk memulai download data.

### tested on windows 11 with Python 3.12.5 

EN version

This repository contains scripts and guidelines for downloading satellite-based rainfall data from the **CMORPH (Climate Prediction Center Morphing Technique)** product with a 30-minute temporal resolution and a spatial resolution of 8x8 km.

## 📌 Description
[CMORPH] (https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/30min/8km/) is a global satellite-based precipitation product developed by NOAA. This dataset features high spatial resolution and is suitable for various applications such as climatology, extreme rainfall analysis, and drought and flood modeling.

## 🗂️ Repository Structure
- `list_data_cmorph.py`
 A Python script to generate a list of CMORPH data URLs, divided into 4 .txt files. It can be modified to cover specific years or an entire date range.

- `download_cmorph_multi.bat` and `download_cmorph_single.bat`
Windows batch files used to download data based on the generated .txt files.

- `README.md` – Documentation for this repository

- ## 📥 How to Use
1. Generate a data list for the desired year(s) using `list_data_cmorph.py`.
2. Place the list and copy the `download_cmorph_multi.bat` and `download_cmorph_single.bat` files into the same folder.
3. Double-click on the `download_cmorph_multi.bat` file to start downloading the data.
