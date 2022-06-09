a=int(input("enter number"))
r=1
while r<=a:
    c=a
    while c>=r:
        print(" ",end=" ")
        c=c-1
    l=1
    while l<=r:
        print(l,end=" ")
        l=l+1
    print()
    r=r+1