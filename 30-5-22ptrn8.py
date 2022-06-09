a=int(input("enter number"))
r=1
while r<=a:
    c=1
    while c<=r:
        print(" ",end="")
        c=c+1
    l=a
    while l>=r:
        print("*",end=" ")
        l=l-1
    print()
    r=r+2