for _ in range(int(input())):
    v,k=map(int,input().split())
    a=-1
    for i in range(v+k):
        if (i*i)%k==v:
            a=i
            break
        if v==0:
            a=0
    print(a)