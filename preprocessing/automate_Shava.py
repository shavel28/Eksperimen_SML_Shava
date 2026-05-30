import os
import kagglehub
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def main():
    print("--- Memulai Proses Preprocessing Otomatis ---")
    path = kagglehub.dataset_download("imakash3011/customer-personality-analysis")
    file_path = os.path.join(path, "marketing_campaign.csv")
    df = pd.read_csv(file_path, sep="\t")
    
    spending_cols = ["MntWines", "MntFruits", "MntMeatProducts", "MntFishProducts", "MntSweetProducts", "MntGoldProds"]
    df["TotalSpending"] = df[spending_cols].sum(axis=1)
    
    median_spending = df["TotalSpending"].median()
    df["Target"] = (df["TotalSpending"] > median_spending).astype(int)
    
    df.drop(columns=["ID", "Dt_Customer"], errors="ignore", inplace=True)
    df.fillna(df.median(numeric_only=True), inplace=True)
    df.drop_duplicates(inplace=True)
    df = pd.get_dummies(df, drop_first=True)
    
    scaler = StandardScaler()
    features = df.drop(columns=["Target"])
    target = df["Target"].reset_index(drop=True)
    
    scaled_features = scaler.fit_transform(features)
    X = pd.DataFrame(scaled_features, columns=features.columns)
    X["Target"] = target
    
    output_path = "preprocessing/customer_preprocessed.csv"
    X.to_csv(output_path, index=False)
    print(f"✔ Selesai! File preprocessed disimpan di: {output_path}")

if __name__ == "__main__":
    main()
