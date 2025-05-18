menu = {
    "Idli": 30,
    "Dosa": 50,
    "Pongal": 45,
    "Vada": 20,
    "Chapati": 40,
    "Parotta": 35,
    "Meals": 80,
    "Lemon Rice": 25}
cart = []
total = 0
print("-------menu-------")
for x , y in menu.items():
    print(f"{x:10} : rs{y:.2f}")
print("------------------")
while True:
    food = input("enter the food you want(q to quit): ")
    if food == "q":
        break
    elif food in menu:
        cart.append(food)
    else:
        print(f"{food} is not on the menu")
print("\n----items selected-----")
for x in cart:
    price = menu.get(x)
    total += menu.get(x)
    print(f"{x:10}-{price:.2f}")
print(f" the total is: rs{total:.2f}")