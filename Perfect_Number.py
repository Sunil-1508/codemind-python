n=int(input())
import math
s=1
for i in range(2,int(math.sqrt(n))+1):
    if(n%i==0):
        s+=i
        s+=n//i
        if(i==n//i):
            s-=i
if(s==n):
    print("True")
else:
    print("False")