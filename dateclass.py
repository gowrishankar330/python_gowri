import datetime

#date = datetime.date(2025,5,23)
#now = datetime.date.today()

#time = datetime.time(13, 56, 9)
#now = datetime.datetime.now()
#now = now.strftime("%H:%M:%S %d-%m-%y")

target_date = datetime.datetime(2025, 5, 23, 13, 56, 59)
cureent_date = datetime.datetime.now()
target_date = target_date.strftime("%H:%M:%S %d-%m-%y")
cureent_date = cureent_date.strftime("%H:%M:%S %d-%m-%y")

#print(time)
#print(now)
#print(time)

if target_date > cureent_date:
    print(f"{target_date} is yet to come")
else:
    print(f"{cureent_date} apna time aagaya")