a=input("enter the main string")
b=input("enter the sub string")
c=''
n=len(a)

index=int(input("enter the vlaue of index"))
for i in range(0,index-1+1,1):
    c=c+a[i]
    print(c)

c=c+b
print(c)


for i in range(index,n-1+1,1):
    c=c+a[i]


print(c)