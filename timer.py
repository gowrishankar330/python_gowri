import time
timer = int(input("enter the duration: "))

for x in range(timer, 0, -1):
    seconds= x%60 
    minutes= int(x/60)%60
    hours= int(x/3600)
    print(f"{hours:03}:{minutes:03}:{seconds:03}")
    time.sleep(2)