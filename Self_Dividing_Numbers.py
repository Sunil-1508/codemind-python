def fun(n):
    t=n
    c=0
    while(n):
        d=n%10
        if(d!=0 and t%(d)==0):
            c+=1
        n//=10
    return c
n=int(input())
m=int(input())
import math
for i in range(n,m+1):
    if(i<10 and i>0):
        print(i,end=' ')
    else:
        d=int(math.log10(i))+1
        if(d==fun(i)):
            print(i,end=' ')