n=int(input())
s=0
for i in range(0,n):
    i=int(input())
    x=i
    s=0
    while(i>0):
        d=int(i%10)
        s=s*10+d
        i=i//10
    if(s==x):
        print("True")
    else:
        print("False")