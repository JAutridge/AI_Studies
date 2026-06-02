import datetime


now = datetime.datetime.now()
date = datetime.date(2026, 4, 11)
time = datetime.time(11, 35, 0)
today = datetime.date.today()

target_datetime = datetime.datetime(2030,12, 25, 5, 30, 5)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target Date has Passed")
else:
    print("Target Date has not passed")
