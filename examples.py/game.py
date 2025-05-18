import random
lowest_num = 5
highest_num = 150
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True
print(f"welcome to number guessing game")
print(f"choose a number between {lowest_num} and {highest_num}")
while is_running:
    guess = input("enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses = guesses + 1
        if guess<lowest_num or guess>highest_num:
            print("enter a valid number")
        elif guess>answer:
            print("number is too high")
        elif guess<answer:
            print("number is too low")
        else:
            print(f"{answer} is correct")
            is_running == False
    else:
        print("enter a valid number")
print(f"you took {guesses} guesses to arrive")