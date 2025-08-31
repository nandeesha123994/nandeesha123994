#hashing

pos=[0 for i in range(10)]
neg=[0 for i in range(10)]

n=int(input("enter the size of n"))
for i in range(0,n-1+1,1):
    x=int(input("enter the values"))
    if x>=0:
        pos[x]=pos[x]+1
    else:
        x=x*-1
        neg[x]=neg[x]+1

print(pos)
print(neg)

print("number - count")

for i in range(10):
    if pos[i]!=0:
     print(i," ",pos[i])

for i in range(10):
    if neg[i]!=0:
     print(i*-1," ",neg[i])


