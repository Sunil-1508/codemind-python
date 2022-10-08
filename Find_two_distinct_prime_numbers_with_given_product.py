def prime(n):
    c=0
    i=1
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    else:
        if(n!=1):
            return True
n=int(input())
import math
for i in range(1,int(math.sqrt(n))+1):
    if(n%i==0):
        x=n
        if(prime(i) and prime(x//i) ):
            print(i,x//i)
            break
else:
    print("-1")