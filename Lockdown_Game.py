n = int(input())
a = []
for i in range(1,n+1):
    a.append(i)
s = input()
si = 0
ci = 0
while(len(a)!=1):
    if s[si]=='y':
        a.pop(ci)
        si+=1
    else:
        si+=1
        ci+=1
    if si>=len(s):
        si=0
    if ci>=len(a):
        ci=0
print(*a)