# l=[1,2,3,4,5]
#
# res=list(map(lambda num:num+10,l))
# print(res)

l=[1,2,3,4,5]

res=list(filter(lambda num:num%2==0, l))
print(res)

