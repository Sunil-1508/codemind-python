n=int(input())
l=list(map(int,input().split()))
s=sum(l)
i=len(l)
while(s%i!=0):
    i-=1
print(i)