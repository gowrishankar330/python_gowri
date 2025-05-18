try:
    number = int(input("enter a number: "))
    divide = 1 / number
    print(divide)
except ZeroDivisionError:
    print("0 vachu kastam pah!")
except ValueError:
    print("loosu koo maari panna koodathu")
except Exception:
    print("something went wrong")
finally:
    print("clean up!")