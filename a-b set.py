# n=int(input('enter the length'))
# a=[int(input()) for i in range(n)]
#
# n=int(input('enter the length'))
# b=[int(input()) for i in range(n)]
#
#
# unique=[]
# for i in a:
#     if i not in b:
#      unique.append(i)
#
#
# print("a=",a)
# print("b=",b)
# print(unique)


n=int(input('enter the length'))
a=[int(input()) for i in range(n)]

n=int(input('enter the length'))
b=[int(input()) for i in range(n)]


unique=[]
for i in b:
    if i not in a:
     unique.append(i)


print("a=",a)
print("b=",b)
print(unique)