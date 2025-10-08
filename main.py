import requests
import json
import time # CRITICAL: Needed for sleep and timestamp
from traffic_yolo import get_car_counts
from traffic_controller import traffic_junction_controller
# from traffic_llm import llm_decision  # Uncomment if using LLM

API_UPDATE_URL = "http://127.0.0.1:5000/update"

# --- HELPER FUNCTION ---
def send_update_to_dashboard(traffic_data):
    """Sends the structured traffic status/counts to the API server."""
    try:
        response = requests.post(API_UPDATE_URL, json=traffic_data)
        if response.status_code != 200:
            print(f"❌ Failed to send dashboard update. Status: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Error: API Server is not running. Please start api_server.py first.")


def run_system(use_llm=False):
    """Runs the continuous traffic analysis and control loop."""
    # We rely on the get_green_time function from the controller for delays
    from traffic_controller import get_green_time

    while True: 
        # 1. Get initial car counts
        counts = get_car_counts() 

        # 2. Get the structured results from the controller
        if use_llm:
            print("🤖 Using LLM for decisions...")
            # ASSUMPTION: Replace with actual LLM controller call
            status_result = {} 
        else:
            print("⚡ Using Rule-Based Controller...")
            # traffic_junction_controller now RETURNS the data dictionary
            status_result = traffic_junction_controller(counts) 
            
        # 3. Send the structured data (dashboard_data) to the API server
        send_update_to_dashboard(status_result['dashboard_data'])

        # 4. Handle Console Output and Time Delays (Simulating Light Cycle)
        total_delay = 0
        
        # Print the console output lines returned by the controller
        for line in status_result['console_output']:
            print(line)

        # Calculate and execute the total delay based on green times
        for dir, cars in status_result['traffic_counts'].items():
            green_time = get_green_time(cars)
            if green_time > 0:
                total_delay += green_time + 2 # Green time + 2s Yellow time

        print(f"🚦 Simulating junction delay of {total_delay}s...")
        time.sleep(total_delay)
        
        print("🔄 Cycle complete. Starting next check in 5 seconds...")
        time.sleep(5) 

if __name__ == "__main__":
    # Ensure all components are running: api_server.py, and autovisualize.py
    run_system(use_llm=False)
