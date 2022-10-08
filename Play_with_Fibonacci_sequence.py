n=int(input())-1
x=0
y=1
print(0,end=" ")
while(n):
    t=x
    x=x+y
    print(x,end=" ")
    y=t
    n-=1