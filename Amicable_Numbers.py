def fun(x):
    s=0
    for i in range(1,x):
        if(x%i==0):
            s+=i
    return s;
n=int(input())
m=int(input())
if(fun(n)==m and fun(m)==n):
    print("Amicable")
else:
    print("Not Amicable")