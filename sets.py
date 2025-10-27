#union and intersection and defferenciation and symmetricdifferenciation

# s1={1,2,3,4}
# s2={1,4,5,6}
#
# print(s1.union(s2))
#
# print(s1.intersection(s2))
#
# print(s1.difference(s2))
#
# print(s1.symmetric_difference(s2))

#set and subset

# s1={1,2,3,4}
# s2={1,2}
#
# print(s1.issubset(s2))
# print(s1.issuperset(s2))
# print(s2.issubset(s1))

#disjoin

# s1={1,2,3,4,5}
# s2={1,4,6,7,8}
# s3={9}
#
# print(s1.isdisjoint(s3))
#
#

#set inside list is not allowed
# s1={1,2,[5,6,7],8,9}                              #set inside list is not allowed
# print(s1)

#set inside tuple is allowed
# s2={1,2,(3,4),5,6}
# print(s2)                                           #set inside the tuple isallowed

#nestes sets are not allowed
s3={1,2,{3,4},5,6}
print(s3)                                            #nested set is not allowwed