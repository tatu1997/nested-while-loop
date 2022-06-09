a=int(input("enter number"))
r=1
while r<=a:
    c=1
    while c<=a-r:
        print(" ",end="")
        c=c+1
    l=1
    while r>=l:
        print("*",end=" ")
        l=l+1
    print()
    r=r+1