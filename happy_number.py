n=int(input())
s=0
while(n>9):
    s=0
    while(n>0):
        d=int(n%10)
        s=s+d*d
        n=n//10
    n=s
if(n==1 or n==7):
    print("True")
else:
    print("False")