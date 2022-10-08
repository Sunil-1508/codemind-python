n=int(input())
s=1
for i in range(0,n):
    s=1
    i=int(input())
    while(i>0):
        s=i*s
        i-=1
    print(s)