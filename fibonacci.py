n=int(input())
x=0
y=1
print("0",end=" ")
while(n-1):
    t=x
    x=x+y
    
    print(x,end=" ")
    y=t
    n-=1