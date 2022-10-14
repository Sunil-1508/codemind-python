v=int(input())
s=0
k=1
while(v>0):
    r=v%10
    k=k*r
    s=s+r
    v=v//10
if(s==k):
    print('Spy Number')
else:
    print('Not Spy Number')