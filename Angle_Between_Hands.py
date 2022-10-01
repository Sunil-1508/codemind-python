s=input()
#print(s)
l=s.split(":")
h,m=map(int,l)
hr=h*30 + m*0.5
mi=m*6
p=abs(hr-mi)
print(min(p,360-p))