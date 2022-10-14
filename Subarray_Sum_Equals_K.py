n,v=map(int,input().split())
vk=list(map(int,input().split()))
s=0
for r in range(n):
    for l in range(r+1,n+1):
        k=sum(vk[r:l])
        if k==v:
            s+=1
print(s)