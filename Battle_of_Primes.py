def fun(n):
    if(n==1):
        return 0
    if(n==2):
        return 1
    import math
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return 0
    return 1
n=int(input())
m=int(input())
c=1
i=1
while(c):
    if(fun(m+n+i)):
        print(i)
        break;
    i+=1