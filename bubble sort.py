# n=int(input("enter the size of n:"))
# a=[]
#
# for i in range(0,n-1+1,1):
#     x=int(input("enter the vlaues"))
#     a.append(x)
# print("before sorted",a)
# for j in range(0,n-1+1,1):
#     for i in range(0,n-2+1,1):
#         if a[i]>a[i+1]:
#             c=a[i]
#             a[i]=a[i+1]
#             a[i+1]=c
#

# print("after sorted list",a)

n=[3,1,4,2]
print(sorted(n))