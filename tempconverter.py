unit = input("enter the unit of temp measured (F or C): ")
temp = float(input("enter the temperature: "))
if unit == "F":
    temp = round((9*temp)/5+32, 1)
    print(f"the temperature in farehiet is: {temp}")
elif unit == "C":
    temp = round((temp-32)*5/9, 1)
    print(f"the temperature in celcius is: {temp}")
else:
    print(f" arivu irukka! {unit} vachu onnum panna mudiyadhu")
