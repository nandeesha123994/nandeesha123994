n=int(input("enter the size of n:"))
a=[]

for i in range(0,n-1+1,1):
    x=int(input("enter the vlaues"))
    a.append(x)
print(a)
i=0
j=n-1
while(i<j):       #repeat the loop util i<j or cross with i cross with j
    c=a[i]
    a[i]=a[j]
    a[j]=c
    i=i+1         #increment the i vlaue
    j=j-1          #decrement value of j
print(a)