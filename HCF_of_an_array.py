n=int(input())
l=list(map(int,input().split()))[:n]
m=min(l)
ans=m
c=0
for i in range(m,0,-1):
    c=0
    for j in l:
        if j%i==0:
            c+=1
    if c==n:
        ans=i
        break
print(ans)