#match case
#an alternative to using many el-if statement



#def day(dayno):
#    match dayno:
#        case 1:
#            return "its sunday"
#        case 2:
#            return "its monday"
#        case 3:
#            return "its tuesday"
#        case 4:
#            return "its wednesday"
#        case 5:
#            return "its thursday"
#        case 6:
#            return "its friday"
#        case 7:
#            return "its saturday"
#        case _:
#            return "not valid"
#user_input = int(input("enter the dayno: "))
#print(day(user_input))


#def weekend(day):
#    match day:
#         case "sunday":
#            return True
#         case "monday":
#            return False
#         case "tuesday":
#            return False
#         case "wednesday":
#            return False
#         case "thursday":
#           return False
#         case "friday":
#            return "its almost weekend!"
#         case "saturday":
#            return True
#         case _:
#            return "not valid"
#user_input = input("enter the day: ")
#print(weekend(user_input))


def weekend(day):
    match day:
        case "sunday" | "saturday":
            return "its weekend baby!"
        case "monday" | "tuesday" | "wednesday" | "thursday":
            return "sad! its weekday"
        case "friday":
            return "get set for weekend mamae"
        case _:
            return "poda punda"
User_input = input("enter ur day: ")
print(weekend(User_input))


