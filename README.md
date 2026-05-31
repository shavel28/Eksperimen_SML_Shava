# Eksperimen Supervised Machine Learning (SML) - Customer Personality Analysis

Repositori ini berisi eksperimen tahap pertama (*Kriteria 1*) untuk proyek **Supervised Machine Learning**. Fokus utama dari repositori ini adalah melakukan pemuatan data, Analisis Data Eksploratif (EDA), dan rekayasa fitur/pembersihan data (*Data Preprocessing*) secara manual maupun otomatis menggunakan pipeline CI/CD.

## 📌 Pemilik Proyek
* **Nama:** Shava Selvia Ramadhani Subekti
* **Username GitHub:** shavel28

---

## 📁 Struktur Repositori (Kriteria 1 Compliance)

Sesuai dengan rekomendasi struktur submission, berkas dalam proyek ini disusun sebagai berikut:

```text
Eksperimen_SML_Shava/
├── .github/
│   └── workflows/
│       └── preprocess.yml                 # Workflow GitHub Actions (Kriteria Advance)
├── customer_personality_analysis_raw/
│   └── marketing_campaign.csv             # Dataset mentah asli dari Kaggle (Raw Data)
├── preprocessing/
│   ├── Eksperimen_Shava.ipynb             # Notebook eksperimen utama & EDA (Template MSML)
│   ├── automate_Shava.py                  # Skrip otonom preprocessing (Kriteria Skilled)
│   └── customer_preprocessed.csv          # File matang hasil akhir preprocessing
└── .gitignore                             # Saringan file sampah lokal (.venv/__pycache__)
```

---

## 📊 Informasi Dataset & Alur Eksperimen

### 1. Sumber Data
Dataset diunduh secara otonom dari Kaggle: `imakash3011/customer-personality-analysis`. Berisi data sosiodemografis pelanggan dan riwayat transaksi belanja mereka.

### 2. Exploratory Data Analysis (EDA)
Di dalam notebook, telah dilakukan analisis komprehensif berupa:
* Pemeriksaan dimensi data, tipe kolom, dan ringkasan statistik deskriptif.
* Identifikasi nilai kosong (*missing values*) dan data duplikat.
* Visualisasi grafik sebaran distribusi dan deteksi pencilan (*outliers*) pada fitur `Income`.

### 3. Data Preprocessing & Feature Engineering
Langkah pembersihan data yang dijalankan mencakup:
* **Feature Engineering:** Penggabungan fitur pengeluaran menjadi `TotalSpending`, serta pembuatan kolom `Target` biner (1: *High Value Customer*, 0: *Low Value Customer*) berdasarkan nilai median populasi.
* **Cleaning:** Penghapusan kolom identitas tak relevan (`ID`, `Dt_Customer`), imputasi nilai kosong menggunakan nilai tengah (*median*), dan penghapusan baris duplikat.
* **Categorical Encoding:** Mengubah fitur teks kategori menjadi representasi angka biner memakai *One-Hot Encoding*.
* **Feature Scaling:** Standardisasi sebaran nilai fitur numerik menggunakan `StandardScaler`.

---

## 🚀 Fitur Otomatisasi (GitHub Actions)

Repositori ini telah dilengkapi dengan sistem integrasi berkelanjutan (**CI/CD**). Setiap kali ada perubahan (*push*) kode ke repositori ini, server cloud GitHub Actions akan otomatis memicu berkas `.github/workflows/preprocess.yml` untuk:
1. Membuka lingkungan virtual berbasis Ubuntu Linux.
2. Memasang seluruh pustaka ketergantungan Python yang dibutuhkan.
3. Mengegsekusi skrip otonom `preprocessing/automate_Shava.py`.
4. Memperbarui dan memastikan data bersih `customer_preprocessed.csv` selalu siap digunakan tanpa intervensi manual.
