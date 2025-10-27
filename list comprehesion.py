

#list comprehesion

l1=[1,2,3,4]

l2=[i for i in l1 if i%2==0]
print(l2)

#writing in long way
l2=[]
for i in l1:
    if i%2==0:
        l2.append(i)
print(l2)