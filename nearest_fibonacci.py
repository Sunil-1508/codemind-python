n=int(input())
x=0
y=1
while(x<n):
    t=x
    x=x+y
    y=t
if abs(n-x)==abs(n-t):
    print(t,x,sep=" ")
elif(abs(n-x)>abs(n-t)):
        print(t)
else:
    print(x)