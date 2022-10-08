def pri(n):
    t=n
    s=0
    while(n>0):
        d=int(n%10)
        s=s*10+d
        n=n//10
    if(s==t):
        return 1
    else:
        return 0
import math
n=int(input())
p=n
s=n-1
n+=1
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
if(x-p>p-y):
    print(y)
elif(x-p<p-y):
    print(x)
else:
    print(y,x)