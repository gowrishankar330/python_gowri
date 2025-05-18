books = {
    "Python Basics": 250,
    "Data Science 101": 400,
    "Machine Learning": 550,
    "Deep Learning": 600,
    "AI for Beginners": 500,
    "Django Web": 350,
    "Flask Essentials": 300,
    "JavaScript Pro": 450}
cart = []
total = 0
print("----items----")
for x , y in books.items():
    print(f"{x:30}:{y:.2f}")
while True:
    item = input("enter the item(q to quit): ")
    if item == "q":
        break
    elif item in books:
        cart.append(item)
    else:
        print(f"{item} is not in the list")
print("---choosen item---")
for i in cart:
    bought = books.get(i)
    total = total + books.get(i)
    print(f"{i:30}:{bought:.2f}")
print(f"total amount to pay: Rs{total}")

