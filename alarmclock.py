import datetime
import time
import pygame

def set_alarm_time(alarm_set):
    print(f"alarm is set to {alarm_set} ")
    sound_file = "/Users/rgowrishankar/python project/morning_flower.mp3"
    is_running = True
     
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        time.sleep(1)

        if current_time == alarm_set:
            print("enthiri mundam")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False

    
if __name__ == "__main__":
    alarm_set = input("enter your alarm time(h:min:sec)= ")
    set_alarm_time(alarm_set)