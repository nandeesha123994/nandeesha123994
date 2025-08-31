a=input("enter the string1")
b=input("enter the string2")
mark=0       #it means equal

if len(a)!=len(b):
    mark=1

else:
    n=len(a)
    for i in range(0,n-1+1,1):
        if a[i]!=b[i]:
            mark=1
            break

if mark==0:
    print("equal")
else:
    print("not equal")