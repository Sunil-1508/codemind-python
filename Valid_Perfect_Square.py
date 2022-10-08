n=int(input())
import math
for i in range(0,n):
    i=int(input())
    x=int(math.sqrt(i))
    if(x*x==i):
        print("True")
    else:
        print("False")