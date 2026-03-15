import pandas as pd

# Load dataset
df = pd.read_csv("Sample_Data_Ingestion.csv")

print("Dataset Loaded Successfully\n")

# Show first 5 rows
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nTotal Records:", len(df))