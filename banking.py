def show_balance(balance):
    print(f"your balance is rs{balance: .2f}")

def deposit_made():
    deposit = float(input("enter the amount to be deposited: "))
    if deposit < 0:
        print(f"{deposit} is not valid!")
        return None
    else:
        return deposit

def withdrawal(balance):
    amount = float(input("enter the amount to withdraw: "))
    if amount < 0:
        print(f"{amount} is not valid!")
        return None
    elif amount>balance:
        print(f"insufficient balance {balance}")
        return None
    else:
        return amount

def main():
    balance = 0
    is_running = True
    while is_running:
            print("welcome to bank program")
            print("press 1. show balance: ")
            print("press 2. deposit: ")
            print("press 3. withdrawal: ")
            print("press 4. exit: ")
            
            choice = int(input("enter an number(1-4): "))
            if choice == 1:
                show_balance(balance)
            elif choice == 2:
                deposit = deposit_made()
                if deposit is not None:
                 balance = balance + deposit
            elif choice == 3:
                amount = withdrawal(balance)
                if amount is not None:
                 balance = balance - amount
            elif choice == 4:
                is_running = False
            else:
                print(f"{choice} is not valid")
    print("thank u have a nice day!")

if __name__ == '__main__':
    main()
