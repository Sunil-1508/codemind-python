n=int(input())
f=0
import math
x=int(math.sqrt(n))
for i in range(1,x+1):
    if(i*(i+1)==n ):
        print("YES")
        f=1
if(f==0):
    print("NO")