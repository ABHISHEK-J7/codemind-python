def sq(a):
    res = 0
    if a == 1:
        return 1
    for i in range(1,a):
        if i*i == a:
            res = 1
            break
    if res == 1:
        return 1
    else:
        return 0
a = int(input())
arr = list(map(int,input().split()))
su = 0
for i in arr:
    if sq(i) == 1:
        su = su + i
print(su)