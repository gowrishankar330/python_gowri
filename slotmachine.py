import random
def spin_row():
    symbols =["🐯","🧠","🤡","💩", "🥸"]
    return [random.choice(symbols) for x in range(3)]

def print_row(row):
    print("----------")
    print(" | " .join(row))
    print("----------")

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🐯":
            return bet * 7
        if row[0] == "🧠":
            return bet * 8
        if row[0] == "🥸":
            return bet * 2
        if row[0] == "🤡":
            return bet * 3
        if row[0] == "💩":
            return bet * 1
    else:
        return 0 

def main():
    balance = 200
    print("welcome to python slot machine game!")
    print("symbols: 🐯 🧠 🤡 💩 🥸")
    while balance>0:
        bet = input("place your bet amount: ")
        if not bet.isdigit():
            print("please enter a valid number")
            continue
        bet = int(bet)
        if bet>balance:
            print("low balance")
            continue
        if bet<=0:
            print("cant be zero or negative")
            continue
        balance = balance - bet

        row = spin_row()
        print_row(row)
        payout = get_payout(row,bet)
        if payout>0:
            print(f"you won rs{payout}")
        else:
            print("sorry you lost!")
        balance = balance + payout
        print(f"your balance is {balance}")
        play_again = input("would u like to play again(y/n): ").lower()
        if play_again != "y":
            break
    print(f"your balance is {balance}")
    print("game over!")


if __name__ == '__main__':
    main()