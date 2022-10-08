a=int(input())
b=int(input())
for i in range(a,b+1):
    x=i
    s=0
    while(i>0):
        d=int(i%10)
        s=s*10+d
        i=i//10
    if(x==s):
        print(x,end=' ')