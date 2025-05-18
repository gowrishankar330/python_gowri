#doubles = []
#for x in range(1,12):
#    doubles.append(x * 2)
#print(doubles)

# expression for value in iterable if condition

#doubles = [(x * 2) for x in range(1,11)]
#print(doubles)

#name = ["gowri", "tripati", "python", "jojo","fucker"]
#upper_name = [(x.upper()) for x in name]
#print(upper_name)

#numbers = [1,-4,-6,4,-5,-9,2,9,-6]
#positive = [ x for x in numbers if x>=0]
#negative = [ x for x in numbers if x<0]
#even = [ x for x in numbers if x % 2 == 0]
#odd = [ x for x in numbers if x % 2 is not 0]
#print(positive)
#print(negative)
#print(even)
#print(odd)

grades =[45,56,89,70,45,67,23,99]

passing_mark = [x for x in grades if x>60]
print(passing_mark)