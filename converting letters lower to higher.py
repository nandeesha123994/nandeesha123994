a=input("enter the string")
b=list(a)
n=len(a)

for i in range(0,n-1+1,1):
    if b[i]>='A' and b[i]<='Z':
        b[i]=chr(ord(b[i])+32)

    elif b[i]>='a' and b[i]<='z':
        b[i] = chr(ord(b[i]) - 32)


print(b)

a=''
for i in b:
    a=a+i

print(a)