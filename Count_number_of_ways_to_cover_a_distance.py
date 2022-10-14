def cn(k):
    if k<0:
        return 0
    if k==0:
        return 1
    return cn(k-1)+cn(k-2)+cn(k-3)
print(cn(int(input())))