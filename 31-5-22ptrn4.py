a=int(input("enter number"))
r=1
while r<=a:
    c=1
    while c<=a:
        if r==1 or r==5 or c==1 or c==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        c=c+1
    print()
    r=r+1
