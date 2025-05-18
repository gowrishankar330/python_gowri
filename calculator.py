operator = input("Please enter an valid operator symbol (+,_,*,/): ")
num1 = float(input("enter 1st number: "))
num2 = float(input("enter 2nd number: "))
if operator == "+":
    result= num1+num2
    print(round(result,1))
elif operator == "-":
    result= num1-num2
    print(round(result,1))
elif operator == "*":
    result= num1*num2
    print(round(result,1))
elif operator == "/":
    result= num1/num2
    print(round(result,1))
else:
    print(f"poda mentalu! {operator} nu oru mayirum kedaiyathu")