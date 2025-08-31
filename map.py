def add(num):
    num=num+10
    return num

l=[1,2,3,4,5]


res=(list(map(add,l)))
print(res)