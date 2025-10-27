#lists are dynamic in nature

# l=[]
# i=0
# while True:
#     print("enter the vlaue")
#     num=int(input(""))
#     l.insert(i,num)
#     i=i+1
#     print("do you want to continue")
#     print("if you wan tpress the 1 other wise print 2")
#     choice=int(input("enter the choice"))
#     if choice==1:
#         continue
#     else:
#         break
#
# print(l)

#nested list

# l=[10,20,["siddu","neelu","pavan"],30,40]
# print(l[2][0])      #siidiu
# print(l[2])         #siddu,neelu,pavan
#

#shaloow copy

l=[10,20,30,40]
l1=l                 #shaloow copy
print(l1)
print(l)
l1[2]=300
print(l1)
print(l)