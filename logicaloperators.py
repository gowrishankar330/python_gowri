temp = 22
is_sunny = True
is_raining = False
if 25<temp<28 and is_sunny and not is_raining:
    print("avoid stepping outside unneccesarily")
elif 18<temp<23 and is_sunny:
    print("enjoy your outdoor activities now")
elif temp<=18 or is_raining:
    print("climate is chill & please be carefull")
elif temp>=28 and is_sunny:
    print("avoid stepping outside")
elif 10<temp<20 or not is_raining:
    print("enjoy the climate")
else:
    print("not sure")