import time

def get_green_time(cars):
    """
    Rule-based timing: more cars → longer green.
    """
    if cars == 0:
        return 0
    elif cars == 1:
        return 4
    else:
        return min(60, 4 + (cars - 1) * 3)  # cap at 60 sec

def traffic_junction_controller(counts):
    """
    Calculates traffic status and timings for all directions and returns the data.
    
    The actual delays (time.sleep) are removed from here.
    """
    directions = ["North", "East", "South", "West"]
    
    # 1. Initialize the dictionary to hold ALL data for the dashboard
    dashboard_data = {
        "Last_Update": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    
    # 2. Prepare the console output (which the main script will print)
    console_output = []

    for dir in directions:
        # Ensure a default count is available
        cars = counts.get(dir, 0) 
        green_time = get_green_time(cars)
        
        # --- Generate Status Strings and Data ---
        
        # Status String (for dashboard/console display)
        if green_time == 0:
            status_string = f"🚫 No cars → Skipping"
            print_line = f"{dir}: {status_string}"
        else:
            status_string = f"🚗 {cars} cars → Green {green_time}s"
            print_line = f"{dir}: {status_string}"

        # 3. Populate the dashboard_data dictionary
        dashboard_data[dir] = status_string
        
        # Add raw counts for autovisualize.py
        dashboard_data[f"{dir}_Count"] = cars
        
        # 4. Prepare the full console output sequence
        console_output.append(print_line)
        if green_time > 0:
            # We add these lines for printing, but do NOT execute time.sleep() here
            console_output.append(f"{dir}: 🟡 Yellow 2s")
            console_output.append(f"{dir}: 🔴 Red")
        console_output.append("") # Blank line separator

    
    # 5. Execute all delays and printing outside of this controller function
    #    to ensure the dashboard update happens *before* the delay.
    
    # We now package the status data AND the console steps into a single return
    return {
        "dashboard_data": dashboard_data,
        "console_output": console_output,
        "traffic_counts": counts # Keep original counts for reference
    }

# NOTE: No `if __name__ == "__main__":` block needed here.x
