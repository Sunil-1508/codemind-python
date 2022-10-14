v=int(input())
s=v
k=0
v=v*v
while(v>0):
    r=v%10
    k=k+r
    v=v//10
if(s==k):
    print('Neon Number')
else:
    print('Not Neon Number')