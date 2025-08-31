a1=input("enter the string1")
b1=input("enter the string2")

a=list(a1)
b=list(b1)

mark=0

if len(a)!=len(b):
    mark=1

else:
    n=len(a)
    for i in range(0,n-1+1,1):
        for j in range(0,n-2,1):
            if a[i]>a[i+1]:
                c=a[i]
                a[i]=a[i+1]
                a[i+1]=c


    for i in range(0,n-1+1,1):
        for j in range(0,n-2,1):
            if b[i]>b[i+1]:
                c=b[i]
                b[i]=b[i+1]
                b[i+1]=c



if a[i]!=b[i]:
    mark=1

if mark==0:
    print("str is angram")