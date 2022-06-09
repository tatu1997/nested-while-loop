a=int(input("enter number"))
r=1
while r<=a:
    c=a
    while c>=r:
      print(" ",end=" ")
      c=c-1
    l=r
    while 0<l:
        print(l,end=" ")
        l=l-1
    print()
    r=r+1