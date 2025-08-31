n=int(input("enter the size of n"))
a=[int(input()) for i in range(n)]

i=0
j=n-1
mark=0

x=int(input("enter the number to be search"))
while(i<=j):
    mid=(i+j)//2
    if x==a[mid]:
        print("found")
        mark=1
        break

    elif x>a[mid]:
        i=mid+1
    else:
        j=mid-1


if mark==1:
    print(x,"element is found","at position",i)















































