n=int(input("enter the size of the list"))
a=[]
for i in range(0,n-1+1,1):
    x=int(input("enter the vlaues"))
    a.append(x)
print(a)


count=0
x=int(input("enter the nuber to seach"))
for i in a:
    if x==i:
        count=count+1
print(count)