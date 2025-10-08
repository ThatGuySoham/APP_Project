import csv, time, requests

API_URL = "http://127.0.0.1:5000/update"
CSV_PATH = "Banglore_traffic_Dataset.csv"

def stream_csv():
    print("🚗 Streaming CSV data to dashboard...")
    with open(CSV_PATH, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            payload = {
                "north": int(row.get("north", 0)),
                "east": int(row.get("east", 0)),
                "south": int(row.get("south", 0)),
                "west": int(row.get("west", 0))
            }
            try:
                requests.post(API_URL, json=payload)
                print("Pushed:", payload)
            except Exception as e:
                print("❌ Error pushing data:", e)
            time.sleep(2)  # every 2 seconds

if __name__ == "__main__":
    stream_csv()
