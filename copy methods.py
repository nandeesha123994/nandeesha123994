# #shallow copy
#
# l=[1,2,3,4,5]
#
# l1=l
#
# print(l1)
# print(l)
#
# l1[2]=300
# print("after modifying")
# print(l1)
# print(l)

#deep copy
#
# l=[1,2,3,4,5]
#
# l1=l.copy()
#
# print(l1)
# print(l)
#
# l1[2]=300
# print("after modifying")
# print(l1)
# print(l)



#in nested list , inner list fallow shallow copy and outer list fallow deep copy

# l=["dale","sindhu",[10,20,30],"habbu"]
#
# l1=l.copy()
#
# print(l)
# print(l1)
#
# l1[2][1]=200          #nested eleme            #fallow shaloow copy
#
# print(l)
# print(l1)

# l1[1]="bindhu"

# print(l)
# print(l1)                    #outer list    #faloow deep copy

#achiving the depp copy inside the nested list

import copy

l=["dale","sindhu",[10,20,30],"habbu"]

l1=copy.deepcopy(l)

print(l)
print(l1)
print("after modifing")
l1[2][1]=200          #nested eleme            #fallow shaloow copy

print(l)
print(l1)

l1[1]="bindhu"
print("after modifying")

print(l)
print(l1)                    #outer list    #faloow deep copy

