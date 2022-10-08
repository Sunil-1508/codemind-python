a,b=map(int,input().split())
min=b
if(a<b):
    min=a
while(min>0):
    if(min%a==0 and min%b==0):
        print(min)
        break
    min+=1