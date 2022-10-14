def sqrt(a):
    for b in range(1,(a//2)+2):
        if b*b==a:
            return 1
    return 0
n=int(input())
v=list(map(int,input().split()))
s=0
for k in range(0,len(v)):
    if sqrt(v[k]):
        s+=v[k]
print(s)