fruits = ["apple", "orange", "pineapple", "grape"]
vegies = ["tomato", "potato", "beans", "carrot"]
drinks = ["beer", "whisky", "vodka", "coke"]

groceries = [fruits,vegies,drinks]

for i in groceries:
    for x in i:
        print(x, end=" ")
    print()

