weight = float(input("enter your weight: "))
unit = input("enter the unit (KILOGRAM or POUNDS): ")
if unit == "KILOGRAM":
    weight = weight * 2.205
    unit = "lbs."
elif unit == "POUNDS":
    weight = weight / 2.205
    unit = ".kgs"
else:
    print(f"{unit} is not valid")
print(f"your weight is: {round(weight,1)} {unit}")
