n=int(input("size of list"))
a=[]
count=0

for i in range(0,n-1+1,1):
    x=int(input("enter the vlaues"))
    a.append(x)

val = int(input("enter the number to be search"))
for i in a:
    if val==i:
       count=count+1
print(count)

