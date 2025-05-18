questions =["how many balls in an over: ",
            "how many balls in an man: ",
            "how many balls in an woman: ",
            "who has the fatest century in ipl: "]
options =[["A.6 ","B.7 ","C.8 ","D.9"],
          ["A.4 ","B.3 ","C.2 ","D.1"],
          ["A.1 ","B.4 ","C.5 ","D.0"],
          ["A.brook ","B.sachin ","C.dhoni ","D.gayle"]]
answers =["A","C","D","D"]
guesses = []
score = 0
question_num = 0

for i in questions:
    print("----------------")
    print(i)
    for x in options[question_num]:
        print(x)
    guess = input(f"enter the correct option(A,B,C,D): ")
    guesses.append(guess)
    if guess == answers[question_num]:
        print("correct!")
        score = score+1
    else:
        print("incorrect")
        print(f"{answers[question_num]} is the correct answer!")
    question_num= question_num+1
print("----results----")
print(score)
print("answers: ",end="")
for x in answers:
    print(x, end="")
print()
print("guesses: ", end="")
for x in guesses:
    print(x, end="")
print()

