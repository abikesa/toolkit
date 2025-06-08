import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load data
soto_2024 = pd.read_csv("../data/soto-2024.csv")
soto_2025 = pd.read_csv("../data/soto-2025.csv")

# Convert 'Date' column to datetime
soto_2024["Date"] = pd.to_datetime(soto_2024["Date"], errors="coerce")
soto_2025["Date"] = pd.to_datetime(soto_2025["Date"], errors="coerce")

# Normalize both to the same year (e.g., 2000) to overlay dates without parallax
soto_2024["PlotDate"] = soto_2024["Date"].apply(lambda d: d.replace(year=2000) if pd.notnull(d) else pd.NaT)
soto_2025["PlotDate"] = soto_2025["Date"].apply(lambda d: d.replace(year=2000) if pd.notnull(d) else pd.NaT)

# Sort by normalized date
soto_2024 = soto_2024.sort_values("PlotDate")
soto_2025 = soto_2025.sort_values("PlotDate")

# Calculate rolling hits (10-game average)
soto_2024["rolling_avg"] = soto_2024["H"].rolling(10).mean()
soto_2025["rolling_avg"] = soto_2025["H"].rolling(10).mean()

# Plot
plt.figure(figsize=(10, 6))
plt.plot(soto_2024["PlotDate"], soto_2024["rolling_avg"], label="Soto Late 2024", linewidth=2)
plt.plot(soto_2025["PlotDate"], soto_2025["rolling_avg"], label="Soto Early 2025", linewidth=2)

# Format x-axis to show only Month-Day
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

# Enhancements
plt.title("Juan Soto Rolling Hits: With vs. Without Judge")
plt.xlabel("Game Date")
plt.ylabel("Hits (10-game rolling avg)")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True, which='major', linestyle='--', linewidth=0.5)
plt.tight_layout()

# Save the figure
plt.savefig("../images/soto-judge-effect.jpeg")
