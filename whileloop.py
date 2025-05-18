#name= input("enter your name: ")
#while not name.find("r") == -1:
#   print("enter a name without r in it!")
#    name = input("enter your name: ")
#print(f"hello {name}")

#food = input("enter your favorite food(q to quit):")
#while not food=="q":
#    print(f" so your favorite is {food}")
#    food = input("enter your favorite food(q to quit):")
#print("bye")
age = int(input("enter your age"))
while age<20 or age>40:
    print(f"{age} is not valid")
    age = int(input("enter your age"))
print("thank you")