import threading
import time


def brush():
    time.sleep(5)
    print("brush your teeth")

def get_milk(name):
    time.sleep(2)
    print(f"get the {name} milk ")

def serve_tea(family, relative):
    time.sleep(4)
    print(f"serve the tea to {family} & {relative}")

task1 = threading.Thread( target=brush)
task1.start()
task2 = threading.Thread(target=get_milk, args=["arokya"])
task2.start()
task3 = threading.Thread(target=serve_tea, args=("appa","mama"))
task3.start()



