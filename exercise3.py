principle= float(input("enter the principle amount: "))
rate= float(input("enter the interest rate: "))
time= float(input("enter the time: "))

while principle<=0:
    print("this value cant be zero")
    principle= input("enter the principle amount: ")
while rate<=0:
    print("this value cant be zero")
    rate= input("enter the interest rate: ")
while time<=0:
    print("this value cant be zero")
    rate= input("enter the time: ")

result = principle * pow((1 + rate / 100), time)
print(f"balance after {time} years is {result:.4f}")    