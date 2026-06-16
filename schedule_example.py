import schedule  # Library that lets you schedule functions to run at specific times
import time      # Used for time.sleep() to pause the loop


# --- SCHEDULED FUNCTIONS ---
# Each function below is a task that will be run automatically
# by the scheduler at the times defined further down

def greeting():
    print("Hello Get UP!")       # Runs every Tuesday at 5:42 PM

def task1():
    print("Task1 Completed")     # Runs every 5 seconds

def task2():
    print("Task2 Completed")     # Runs every 10 seconds

def task3():
    print("Task3 Completed")     # Runs every 15 seconds


# --- SCHEDULING THE TASKS ---
# schedule.every() sets up when each function should run
# .do(function) tells the scheduler WHICH function to call

# Runs greeting() every Tuesday at exactly 5:42 PM
schedule.every().tuesday.at("17:42").do(greeting)

# Runs task1() every 5 seconds
schedule.every(5).seconds.do(task1)

# Runs task2() every 10 seconds
schedule.every(10).seconds.do(task2)

# Runs task3() every 15 seconds
schedule.every(15).seconds.do(task3)


# --- MAIN LOOP ---
# This loop runs forever (until you press Ctrl+C to stop it)
# run_pending() checks if any scheduled task is due to run
# time.sleep(1) waits 1 second before checking again
# Without this loop, the program would exit immediately
while True:
    schedule.run_pending()  # Check and run any tasks that are due
    time.sleep(1)           # Wait 1 second before checking again