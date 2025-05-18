#validate use input exercise
#1. username is no more than 10 characters
#2. username cannot contain spaces
#3. username must not have any digits

username= input(" enter ur username: ")

if len(username) > 12:
    print(" your usename cannot have more than 12 letters")
elif not username.find(" ") == -1:
    print(" your username cannot have spaces")
elif not username.isalpha():
    print(" your username cannot have digits")
else:
    print(f"welcome {username}")
