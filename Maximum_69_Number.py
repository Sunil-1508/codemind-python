n=int(input())
s=str(n)
for i in range(len(s)):
    if s[i]=='6':
        s=s.replace(s[i],'9',1)
        break
print(s)