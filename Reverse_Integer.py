x=int(input())
if x<0:
    t=1
    x=x*-1
else:
    t=0
s=str(x)
s=s[::-1]
ans=int(s)
if (ans>=-(2**31)) and (ans<=(2**31)-1):
    if t==1:
        print(-1*ans)
    else:
        print(ans)
else:
    print(0)