n=int(input('enter the length'))
a=[int(input()) for i in range(n)]

n=int(input('enter the length'))
b=[int(input()) for i in range(n)]


inter=[]
for i in a:
    if i in b:
     inter.append(i)


print("a=",a)
print("b=",b)
print(inter)