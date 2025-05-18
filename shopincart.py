foods = []
prices = []
total = 0

while True:
    food = input("select the food(q to quit): ") 
    if food == "q":
        break
    else:
        price = float(input("enter the price of food: "))
        foods.append(food)
        prices.append(price)
print(f"-----your order summary------")
for i in range(len(foods)):
    print(f"({foods[i]} - rs{prices[i]:.2f}")
print(f"total item {len(foods)}")
total= sum(prices)
print(f"total price of item {total}")
