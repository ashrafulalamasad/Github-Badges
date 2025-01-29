import os
from datetime import datetime, timedelta
import time

def makeCommits(start_date: str, end_date: str):
    # Parse the start and end dates
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    # Check if the start date is before or equal to the end date
    if start_date > end_date:
        print("Invalid range. Ensure start_date is before or equal to end_date.")
        return

    current_date = start_date
    while current_date <= end_date:
        formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
        # Create an empty commit with the specified date
        os.system(f'git commit --allow-empty --date="{formatted_date}" -m "Commit for {formatted_date}"')
        current_date += timedelta(days=1)  # Move to the next day

    os.system('git push')

def runMultipleTimes(start_date: str, end_date: str, num_times: int, interval_sec: int):
    for _ in range(num_times):
        makeCommits(start_date, end_date)
        time.sleep(interval_sec)  # Wait for the specified interval in seconds

# Run the function multiple times with a 5-second break
runMultipleTimes(start_date="2024-11-06", end_date="2025-01-28", num_times=2, interval_sec=0.1)




