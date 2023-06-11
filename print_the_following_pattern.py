a = int(input())
for i in range(a):
    for j in range(a):
        if i==j:
            print("x",end="")
        elif i+j == a-1:
            print("x",end="")
        else:
            print("0",end="")
    print()