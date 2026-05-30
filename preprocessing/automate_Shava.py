import os
import kagglehub
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def main():
    print("--- Memulai Proses Preprocessing Otomatis ---")
    
    # 1. Download Dataset dari Kaggle
    print("Mendownload dataset dari Kaggle...")
    path = kagglehub.dataset_download("imakash3011/customer-personality-analysis")
    print(f"Dataset berhasil diunduh ke: {path}")
    
    # 2. Load Dataset (Menggunakan pemisah Tab '\t')
    file_path = os.path.join(path, "marketing_campaign.csv")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File marketing_campaign.csv tidak ditemukan di {path}")
        
    df = pd.read_csv(file_path, sep="\t")
    print(f"Data berhasil dimuat. Ukuran awal: {df.shape}")
    
    # 3. Feature Engineering: Total Spending & Target Label
    print("Menjalankan Feature Engineering...")
    spending_cols = [
        "MntWines", "MntFruits", "MntMeatProducts", 
        "MntFishProducts", "MntSweetProducts", "MntGoldProds"
    ]
    df["TotalSpending"] = df[spending_cols].sum(axis=1)
    
    # Membuat Target berdasarkan nilai Median (1: High Value, 0: Low Value)
    median_spending = df["TotalSpending"].median()
    df["Target"] = (df["TotalSpending"] > median_spending).astype(int)
    
    # 4. Data Cleaning (Hapus Kolom & Isi Missing Value)
    print("Melakukan Data Cleaning...")
    df.drop(columns=["ID", "Dt_Customer"], errors="ignore", inplace=True)
    
    # Imputasi missing value pada kolom numerik dengan median
    df.fillna(df.median(numeric_only=True), inplace=True)
    
    # Hapus data duplikat
    df.drop_duplicates(inplace=True)
    
    # 5. Encoding Variabel Kategorikal
    print("Melakukan Categorical Encoding...")
    df = pd.get_dummies(df, drop_first=True)
    
    # 6. Scaling Fitur (Kecuali Target)
    print("Melakukan Feature Scaling...")
    scaler = StandardScaler()
    
    features = df.drop(columns=["Target"])
    target = df["Target"].reset_index(drop=True)
    
    scaled_features = scaler.fit_transform(features)
    X = pd.DataFrame(scaled_features, columns=features.columns)
    
    # Gabungkan kembali fitur yang sudah diskalakan dengan Target
    X["Target"] = target
    
    # 7. Simpan Hasil ke CSV
    output_path = "preprocessing/customer_preprocessed.csv"
    X.to_csv(output_path, index=False)
    print(f"✔ Selesai! File preprocessed disimpan di: {output_path}")
    print(f"Ukuran data akhir: {X.shape}")

if __name__ == "__main__":
    main()