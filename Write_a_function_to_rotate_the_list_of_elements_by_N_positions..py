n=int(input())
vk=list(map(int,input().split()))
rot=int(input())
for _ in range(rot):
    t=vk[-1]
    for r in range(len(vk)-1,0,-1):
        vk[r]=vk[r-1]
    vk[0]=t
print(*vk)