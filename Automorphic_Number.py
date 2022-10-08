n=int(input())
n=abs(n)
x=abs(n)
r=n*n
c=0
v=0
while(abs(n)>0):
    d=n%10
    n=n//10
    c+=1
i=0
while(i<c):
    if(r%10==x%10):
        v+=1
        r=r//10 
        x=x//10
    else:
        break
    i+=1
if(c==v):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")