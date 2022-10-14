for _ in range(int(input())):
    _=int(input())
    v=list(map(int,input().split()))
    k=sorted(v)
    if v==k:
        print(0)
    else:
        print(k[-1]-k[0])