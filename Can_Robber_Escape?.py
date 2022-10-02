n=int(input())
o=0
a=list(map(int,input().split()))[:n]
for i in a:
    if(i%2==1):
        o+=1
if(o<=2):
    print("YES")
else:
    print("NO")