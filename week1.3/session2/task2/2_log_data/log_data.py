# Week 1.3, Session 2: Log Data Filtering

import csv
from pathlib import Path

log_file = Path(__file__).with_name("site.log")

try:
    with log_file.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header row

        for row in reader:
            if len(row) < 6:
                continue

            date, time, ip_address, user_agent, request, status_code = row

            if request == "POST /login" and status_code == "401":
                print(f"IP address {ip_address} failed to login at {time} on {date}")

except FileNotFoundError:
    print(f"Could not find {log_file.name}")

# We want to find all failed login attempts based on Request and Status code
# (i.e., POST /login with the response 401) in a log file and print these out in a
# human-readable format.

# The script above prints entries in the format:
# IP address 192.168.1.17 failed to login at 10:42:12 on 2024-10-20