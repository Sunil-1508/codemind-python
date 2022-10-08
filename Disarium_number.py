n=int(input())
t=n
s=0
c=0
a=n
while(n!=0):
    n=n//10
    c+=1
while(t!=0):
    d=t%10
    t=t//10
    s+=d**c
   # print(s)
    c-=1
    
#print(t,  s)
if(a==s):
    print(True)
else:
    print(False)