n=int(input())
l=list(map(int,input().split()))
d={}
p=[]
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for k,v in d.items():
    if k==v:
        p.append(k)
if p==[]:
    print(-1)
else:
    print(min(p),max(p),sep=" ")