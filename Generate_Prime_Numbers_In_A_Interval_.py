def fun(n):
    if(n==1):
        return 0
    if(n==2):
        return 1
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return 0
    else:
        return 1
n=int(input())
m=int(input())
import math
for i in range(n,m+1):
    if(fun(i)):
        print(i)