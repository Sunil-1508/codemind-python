def pri(n):
    if(n==1):
        return 0
    if(n==2):
        return 1
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return 0
    return 1
import math
n=int(input())
p=n
s=n
while(n):
    if(pri(n)):
        x=n
        break
    n+=1
while(s):
    if(pri(s)):
        y=s
        break
    s-=1
if(x-p>=p-y):
    print(p-y)
else:
    print(x-p)