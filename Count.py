n=int(input())
v=list(map(int,input().split()))
a=b=0
for k in range(0,len(v)):
    if v[k]%2==0:
        a+=1
    else:
        b+=1
print(a,b,end=' ')