n=int(input())
vk=list(map(int,input().split()))
for l in range(len(vk)):
    a=l
    b=-1
    for j in range(l+1,len(vk)):
        if(vk[l]<vk[j]):
            b=j
            break
    if(b==-1):
        a=0
    else:
        a=b-a
    print(a,end=' ')