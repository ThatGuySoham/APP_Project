import requests
import matplotlib.pyplot as plt
import time
import os

# --- Configuration ---
API_URL = "http://localhost:5000/traffic_counts"  # Replace if different
SAVE_FOLDER = "dashboard/visuals"
INTERVAL = 60  # in seconds, adjust as needed

# Ensure save folder exists
os.makedirs(SAVE_FOLDER, exist_ok=True)

def fetch_traffic_counts():
    try:
        response = requests.get(API_URL)
        data = response.json()
        return data  # expects {'North': 120, 'South': 80, 'East': 100, 'West': 60}
    except:
        # fallback if API fails
        return {'North': 0, 'South': 0, 'East': 0, 'West': 0}

def create_charts(data):
    directions = list(data.keys())
    vehicle_counts = list(data.values())
    total = sum(vehicle_counts)

    # Bar chart
    plt.figure(figsize=(8,5))
    plt.bar(directions, vehicle_counts, color=['skyblue', 'lightgreen', 'orange', 'salmon'])
    plt.title('Traffic Count by Direction')
    plt.xlabel('Direction')
    plt.ylabel('Number of Vehicles')
    bar_path = os.path.join(SAVE_FOLDER, "traffic_bar_chart.png")
    plt.savefig(bar_path)
    plt.close()

    # Pie chart
    plt.figure(figsize=(6,6))
    plt.pie(vehicle_counts, labels=directions, autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'orange', 'salmon'])
    plt.title('Traffic Distribution by Direction')
    pie_path = os.path.join(SAVE_FOLDER, "traffic_pie_chart.png")
    plt.savefig(pie_path)
    plt.close()

    # Summary table
    table_path = os.path.join(SAVE_FOLDER, "traffic_summary.txt")
    with open(table_path, "w") as f:
        f.write("--- Traffic Summary ---\n")
        f.write(f"{'Direction':<10} | {'Vehicle Count':<13} | {'% of Total':<10}\n")
        f.write("-"*40 + "\n")
        for dir, count in data.items():
            pct = (count / total * 100) if total else 0
            f.write(f"{dir:<10} | {count:<13} | {pct:>7.1f}%\n")

    print(f"Charts and summary updated in {SAVE_FOLDER}")

# --- Main Loop ---
if __name__ == "__main__":
    while True:
        counts = fetch_traffic_counts()
        create_charts(counts)
        time.sleep(INTERVAL)
