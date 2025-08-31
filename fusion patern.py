#merging of left triangle and right trinagle

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
#     print(" ")


# n=3
# for i in range(1,3+1,1):
#     for j in range(1,n-i+1,1):
#         print("  ",end="")
#     for j in range(1,i+1,1):
#         print("* ",end="")
#     for j in range(1,i-1+1,1):
#         print("* ",end="")
#     print("")
#
# n=2
# for i in range(1,2+1,1):
#     for j in range(1,i+1,1):
#         print("  ",end="")
#     for j in range(1,n-i+1,1):
#         print("* ",end="")
#     for j in range(1,n-i+1+1,1):
#         print("* ",end="")
#     print("")
#

# n=3
# for i in range(1,3+1,1):
#      for j in range(1,n-i+1,1):
#          print("  ",end="")
#      for j in range(1,i+1-1,1):
#          print("* ",end="")
#      for j in range(1, i + 1, 1):
#          print("* ", end="")
#
#      print(" ")
#
# n=2
# for i in range(1,2+1,1):
#      for j in range(1,i+1,1):
#           print("  ",end="")
#      for j in range(1, n-i+1+1-1, 1):
#           print("* ", end="")
#      for j in range(1, n - i + 1 + 1, 1):
#           print("* ", end="")
#      print("")
#
# number and star triangler
# n=5
# for i in range(1,5+1,1):
#      for j in range(1,i+1,1):
#           print("* ",end="")
#      for j in range(1,n-i+1,1):
#           print(i,"",end="")
#      print("")

#right triangle +decending nubers
# n=5
# for i in range(1,5+1,1):
#      for j in range(1,i+1,1):
#           print("* ",end="")
#      for j in range(1,1+1,1):
#           print(n,"",end="")
#           n=n-1
#      print("")
#
#mirror number -star fusion
# n=5
# for i in range(1,5+1,1):
#      for j in range(1,n-i+1,1):
#           print("& ",end="")
#      for j in range(1,1+1,1):
#           print(i," ",end="")
#      for j in range(1,i+1,1):
#           print("* ",end="")
#      print("")

#nubers + stars in fusion
# n=5
# for i in range(1,5+1,1):
#      for j in range(1,n-i+1+1,1):
#           print(i,"",end="")
#      for j in range(1,i-1+1,1):
#           print("* ",end="")
#
#      print()

#zigzag fusion
# n=5
# for i in range(1,5+1,1):
#      for j in range(1,i+1,1):
#           if i%2==0:
#                print("*",end="")
#           else:
#                print(i,end="")
#      print("")


#diamond
# n=4
# for i in range(1,4+1,1):
#      for j in range(1,n-i+1+1,1):
#           print("*",end="")
#      for j in range(1,i-1+1,1):
#            print("$"*2,end="")
#      for j in range(1,n-i+1+1,1):
#           print("*",end="")
#
#      print("")
# #
# n=4
# for i in range(1,4+1,1):
#      for j in range(1,i+1,1):
#           print("*",end="")
#
#      for j in range(1,n-i+1,1):  #4-1+1=4 printed 3 times, multiply in to (2) it becomes (6)
#           print("$"*2,end="")
#
#      for j in range(1,i+1,1):
#           print("*",end="")
#      print("")

#rambhous
# n=4
# for i in range(1,4+1,1):
#     for j in range(1,4+1,1):
#         if i+j==n+1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     for j in range(1,4+1,1):
#         if i==j+1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#
#     print("")
#
#
# n=3
# for i in range(1,3+1,1):
#     for j in range(1,3+1,1):
#         if i==j-1: #eg 5==6 do -1
#             print("*",end="")
#         else:
#             print(" ",end="")
#     for j in range(1,3+1,1):
#         if i+j==n+1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("")
