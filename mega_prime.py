v=int(input())
a=0
c=0
for i in range(1,v+1,1):
    if v%i==0:
        c+=1    
if c!=2:
    print('Not Mega Prime')
else:
    while v:
        r=v%10
        c=0
        for i in range(1,r+1,1):
               if r%i==0:
                c+=1
        if c!=2:
            a+=1
        v=v//10
    if a==0:
        print('Mega Prime')
    else:
        print('Not Mega Prime')