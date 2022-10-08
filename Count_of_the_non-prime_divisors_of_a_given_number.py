def fun(n):
    if(n==1):
        return 1
    if(n==2):
        return 0
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return 1
    else:
        return 0
n=int(input())
import math
c=0
for i in range(1,int(math.sqrt(n))+1):
    if(n%i==0):
        if(fun(i)):
            c+=1
        if(fun(n//i)):
            c+=1
        if(i==n//i):
            c-=1
print(c)