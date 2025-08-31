# n=3
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print("* ",end="")
#     for j in range(1, n - i + 1, 1):
#         print("& ", end="")
#     for j in range(1, n - i+1 + 1, 1):
#         print("$ ", end="")
#     for j in range(1,i,1):
#         print("* ",end="")
#     for j in range(1,1+1,1):
#         print("* ",end="")
#
#
#
#     print(" ")


# n=3
# for i in range(1,n+1,1):
#     for j in range(1,n-i+1,1):
#         print("  ",end="")
#     for i in range(1,i+1,1):
#         print("* ",end="")
#     for i in range(1,i,1):
#         print("* ",end="")
#     print("")
#
# n=2
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print("  ",end="")
#     for j in range(1,n-i+1,1):
#         print("* ",end="")
#     for j in range(1,n-i+1+1,1):
#         print("* ",end="")
#
#     print("")



# n=5
# for i in range(1,5+1,1):
#     for j in range(1,n-i+1+1,1):
#         print(i,end=" ")
#     for j in range(1,i,1):
#         print("* ",end="")
#     print("")
#

# n=5
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         if i%2==0:
#             print("*",end="")
#         else:
#             print(i,end="")
#     print("")



# n=5
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print("* ",end="")
#     for j in range(1,1+1,1):
#         print(n,"",end="")
#         n=n-1
#     print("")

# n=4
# for i in range(1,n+1,1):
#     for j in range(1,n+1,1):
#         if i+j==n+1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#
#     for j in range(1,n+1,1):
#         if i==(j+1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("")
#
#
# n=3
# for i in range(1,n+1,1):
#     for j in range(1,n+1,1):
#         if i==(j-1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     for j in range(1,n+1,1):
#         if i+j==n+1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#
#     print("")
#


# n=3
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print("* ",end="")
#     for j in range(1,n-i+1,1):
#         print("& "*2,end="")
#     for j in range(1,i+1,1):
#         print("* ",end="")
#     print("")

# n=4
# for i in range(1,n+1,1):
#     for j in range(1,n+1,1):
#         if i==1 or j==1 or i==4:
#             print("% ",end="")
#         else:
#             print(" ",end="")
#     for j in range(1,n+1-2, 1):
#         if  i==1 or i==4 or j==1:      #body
#             print("# ", end="")
#         else:
#             print(" ", end="")
#     for j in range(1,n+1, 1):
#         if  i==3 or i==4:
#             print("@ ", end="")
#         else:
#             print(" ", end="")
#     print("")

n=3
for i in range(1,n+1,1):
    for j in range(1,2+1,1):
        print("* ",end="")
    for j in range(1,2+1,1):
        print("& ",end="")
    for j in range(1,2+1,1):
        print("* ",end="")

    print("")















