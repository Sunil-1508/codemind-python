n=int(input())
t=n
c=0
while(t):
    r=t%10
    p=1
    while(r):
        p*=(r)
        r-=1
    c+=p
    t//=10
if c==n:
    print("The number "+str(n)+" is a strong number")
else:
    print("The number "+str(n)+" is not a strong number")