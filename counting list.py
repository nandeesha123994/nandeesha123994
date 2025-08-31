a=[]
n=int(input("enter the size of n:"))
count=0
for i in range(1,n+1,1):
    x=int(input("enter the vlaues:"))
    a.append(x) #attach the vlaues aat the end
# print(a)
val=int(input("enter the vlaue to be seacrch:"))
for i in a:
     if val==i:
         count=count+1
print(count)