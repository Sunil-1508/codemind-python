import math
def fun(n):
    if(n==1):
        return 0
    if(n==2):
        return 1
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return 0
    else:
        return 1;
n=int(input())
if fun(n)==1:
    print("prime")
else:
    print("not a prime")