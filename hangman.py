import random
words = [ "apple", "orange", "blueberry", "strawberry", "ginger"]

hangman_art ={0:"hey",
              1:"you",
              2:"are",
              3:"going",
              4:"to",
              5:"lose",
              6:"& you did!"}

def hangman_display(wrong_guesses):
        print(hangman_art[wrong_guesses])

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint =["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        hangman_display(wrong_guesses)
        display_hint(hint)
        guess = input("enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("invalid guess!")
            continue
        if guess in guessed_letters:
            print(f"{guess} is already guessed!")
            continue
        guessed_letters.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses = wrong_guesses + 1
        if "_" not in hint:
            hangman_display(wrong_guesses)
            display_answer(answer)
            print("you win!")
            is_running = False
        elif wrong_guesses >= 6:
            print("game over")
            print(f"the word was {answer}")
            break

if __name__== "__main__":
    main()