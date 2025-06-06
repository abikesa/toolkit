import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# === Step 1: Generate random dataset ===
np.random.seed(42)  # for reproducibility

num_rows = 500
data = {
    "CustomerID": np.arange(1, num_rows + 1),
    "Age": np.random.normal(loc=35, scale=10, size=num_rows).astype(int),
    "Income": np.random.normal(loc=60000, scale=15000, size=num_rows).astype(int),
    "PurchaseAmount": np.random.exponential(scale=300, size=num_rows).round(2)
}

df = pd.DataFrame(data)

# Optional: Clean age/income to realistic bounds
df["Age"] = df["Age"].clip(lower=18, upper=80)
df["Income"] = df["Income"].clip(lower=20000, upper=200000)

# === Step 2: Save to CSV ===
csv_path = "../data/synthetic_customers.csv"
df.to_csv(csv_path, index=False)
print(f"✅ Dataset saved to {csv_path}")

# === Step 3: Read dataset ===
df_read = pd.read_csv(csv_path)

# === Step 4: Analyze and plot ===
plt.figure(figsize=(10, 6))
plt.scatter(df_read["Income"], df_read["PurchaseAmount"], alpha=0.5)
plt.title("Income vs Purchase Amount")
plt.xlabel("Income ($)")
plt.ylabel("Purchase Amount ($)")
plt.grid(True)

# === Step 5: Save plot as JPEG ===
jpeg_path = "../outputs/soto-analysis-0.jpeg"
plt.savefig(jpeg_path, format="jpeg")
print(f"📸 Plot saved as {jpeg_path}")

