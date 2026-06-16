import datetime

# --- CURRENT DATE AND TIME ---
# datetime.now() returns the current date AND time together
# Example output: 2026-06-16 10:30:45.123456
now = datetime.datetime.now()

# --- SPECIFIC DATE ---
# datetime.date() creates a specific date with year, month, day
# This creates: April 11, 2026
date = datetime.date(2026, 4, 11)

# --- SPECIFIC TIME ---
# datetime.time() creates a specific time with hour, minute, second
# This creates: 11:35:00 AM
time = datetime.time(11, 35, 0)

# --- TODAY'S DATE ---
# datetime.date.today() returns only today's DATE (no time)
# Example output: 2026-06-16
today = datetime.date.today()

# --- TARGET DATETIME ---
# Creates a specific date AND time in the future to compare against
# This is Christmas Day 2030 at 5:30:05 AM
target_datetime = datetime.datetime(2030, 12, 25, 5, 30, 5)

# --- CURRENT DATETIME ---
# Gets the current date and time at the moment this line runs
# Used to compare against the target datetime
current_datetime = datetime.datetime.now()

# --- DATE COMPARISON ---
# Compares target_datetime against current_datetime
# datetime objects can be compared using < > == just like numbers
if target_datetime < current_datetime:
    # Target date is in the PAST
    print("Target Date has Passed")
else:
    # Target date is in the FUTURE
    print("Target Date has not passed")