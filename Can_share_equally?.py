x,y=map(int,input().split())
if(x==0 and y%2==1):
    print("NO")
if(x%2==0 and y%2==1 and x!=0):
    print("YES")
if(y%2==0 and x%2==0):
    print("YES")
if(x%2==1 and x!=0):
    print("NO")