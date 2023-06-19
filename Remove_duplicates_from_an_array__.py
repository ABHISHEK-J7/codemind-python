n = int(input())
arr = list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if i != j:
            if arr[i] == arr[j] and arr[i] != -1:
                arr[j] = -1
for i in range(n):
    if arr[i] != -1:
        print(arr[i],end = " ")
    
    
    