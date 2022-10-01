n=int(input())
l=list(map(int,input().split()))[:n]
e=o=0
for i in l:
    if i%2==0:
        e+=1
    else:
        o+=1
if e%2==0 and o%2==0:
    print(1)
else:
    print(0) 