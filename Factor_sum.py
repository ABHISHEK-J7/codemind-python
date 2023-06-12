arr = list(map(int,input().split(',')))
arr2 = []
c = 0
for i in range(len(arr)):
    s = 0
    v = arr[i]
    for j in range(1,v+1):
        if v%j == 0:
            s+=j
    if s in arr:
        arr2.append(v)
        c+=1
if c == 0:
    print(-1)
else:
    arr2.sort()
    for i in arr2:
        print(i,end=" ")