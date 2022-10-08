n=int(input())
t="0"*(n)
for i in range(0,int(2**n)):
    s=t+bin(i)[2:]
    print(s[-n:])