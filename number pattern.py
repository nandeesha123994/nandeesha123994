#right trinagle
# n=5
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print(1,end=" ")
#     print("")
#

#left triangle
# n=5
# for i in range(1,n+1,1):
#     for j in range(1,n-i+1+1,1):
#         print(1,end=" ")
#     print("")

#hill pattern

# n=4
# for i in range(1,n+1,1):
#     for j in range(1,n-i+1+1,1):
#         print("*",end="")
#     for j in range(1,i+1,1):
#         print(1,end="")
#     for j in range(1,i+1-1,1):
#         print(1,end="")
#     print(" ")

#invertedd hill pattern

# n=5
# for i in range(1,n+1,1):
#     for j in range(1,i-1+1):
#         print("*",end="")
#     for j in range(1,n-i+1+1,1):
#         print(1,end="")
#     for j in range(1,n-i+1,1):
#         print(1,end="")
#     print("")

#dimond

# n=4
# for i in range(1,n+1,1):
#     for j in range(1,n-i+1+1,1):
#         print(" ",end="")
#     for j in range(1,i+1,1):
#         print(1,end="")
#     for j in range(1,i+1-1,1):
#         print(1,end="")
#     print(" ")

# n = 5
# for i in range(1,n+1,1):
#     for j in range(1,i-1+1):
#         print(" ",end="")
#     for j in range(1,n-i+1+1,1):
#         print(1,end="")
#     for j in range(1,n-i+1,1):
#         print(1,end="")
#     print("")
#

#
# n=5
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print(i,end=" ")
#     print("")

#increasing number pattern oreder
# n=5
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print(n-i+1,end=" ")
#     print("")


# n=5
# p=5
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print(p,end=" ")
#     p=p-1
#     print("")




# n=5
# p=0
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print(p,end="")
#     p=p+2
#     print("")


#
# n=5
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         if i==1 or i==3 or i==5:
#             print(1,end="")
#         else:
#             print(2,end="")
#     print("")


# n=5
# for i in range(1,n+1,1):
#     for j in range(1,i+1-1,1):
#         print("*",end="")
#     for j in range(1,n-i+1+1,1):
#         if i==1 or i==3:
#             print("#",end="")
#         else:
#             print("$",end="")
#     print("")






#flyoid trinagle

# n=5
# p=1
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print(p,end="")
#         p=p+1
#     print(" ")