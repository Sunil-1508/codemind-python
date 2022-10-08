n=int(input())
a=[]
while(n):
    a.append(n%10)
    n//=10
s=set(a)
if(len(a)==len(s)):
    print("Unique Number")
else:
    print("Not Unique Number")