n = int(input())
l = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","T","U","V","W","X","Y","Z"]
for i in range(n,0,-1):
    for j in range(i):
        print(l[i-1],end=" ")
    print()