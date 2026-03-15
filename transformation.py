import pandas as pd
import hashlib

# Load dataset
df = pd.read_csv("Sample_Data_Ingestion.csv")

print("Dataset Loaded for Transformation")

# Convert timestamp column
df["Log_Timestamp"] = pd.to_datetime(df["Log_Timestamp"], format="%d-%m-%Y %H:%M")

# CPU status classification
df["CPU_Status"] = df["CPU_Utilization (%)"].apply(
    lambda x: "Critical" if x > 85 else "Normal"
)

# Memory status classification
df["Memory_Status"] = df["Memory_Usage (%)"].apply(
    lambda x: "Critical" if x > 90 else "Normal"
)

# Server availability calculation
df["Availability (%)"] = (
    df["Uptime (Hours)"] /
    (df["Uptime (Hours)"] + df["Downtime (Hours)"])
) * 100

# Encrypt sensitive fields
def encrypt(value):
    return hashlib.sha256(str(value).encode()).hexdigest()

df["IP_Address"] = df["IP_Address"].apply(encrypt)
df["Admin_Email"] = df["Admin_Email"].apply(encrypt)
df["Admin_Phone"] = df["Admin_Phone"].apply(encrypt)

# Save processed dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nTransformation Completed Successfully")
print(df.head())