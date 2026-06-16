import schedule
import time

def greeting():
    print("Hello")

def task1():
    print("Task1 Completed")

def task2():
    print("Task2 Completed")

def task3():
    print("Task3 Completed")

schedule.every().thursday.at("14:05").do(greeting)
schedule.every(5).seconds.do(task1)
schedule.every(10).seconds.do(task2)
schedule.every(15).seconds.do(task3)


while True:
    schedule.run_pending()
    time.sleep(1)



