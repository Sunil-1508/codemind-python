n=int(input())
l=list(map(int,input().split()))[:n]
m=max(l)
ans=m
c=0
i=m
while(True):
    c=0
    for j in l:
        if i%j==0:
            c+=1
    if c==n:
        ans=i
        break
    else:
        i+=m
    
print(ans)
