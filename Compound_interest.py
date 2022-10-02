p,r,t=map(int,input().split())
import math
a=p*pow((1+r/100),t)
print("{:.2f}".format(a))