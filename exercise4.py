num_pad = [[1,2,3],
           [4,5,6],
           [7,8,9],
           ["*",0,"#"]]
for i in num_pad:
    for y in i:
        print(y, end="")
    print()