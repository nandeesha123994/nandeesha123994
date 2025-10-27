# import pickle
#
# class employee:
#     def __init__(self,name,age):
#         self.age=age
#         self.ename=name
#
#     def disp(self):
#         print(self.ename)
#         print(self.age)
# e=employee("nandi",21)
#
# ptr=open("nandeesha.txt","wb")
# pickle.dump(e,ptr)
# ptr.close()

#
# import pickle
#
# class employee:
#     def __init__(self,name,age):
#         self.age=age
#         self.ename=name
#
#     def disp(self):
#         print(self.ename)
#         print(self.age)
#
# f=open("nandeesha.txt",'rb')
# e=pickle.load(f)
# e.disp()
# print("obj is retrived")
# f.close()


import pickle
fruits=["apple","banan"]

f=open("fruitss.txt","wb")
pickle.dump(fruits,f)
f.close()

f=open("fruits.txt","rb")
ptr=pickle.load(f)
print(ptr)
f.close()


# x = [12, 34]
# print(len(''.join(list(map(int, x)))))

# num=1234
# sumeven=0
# oddeven=0
#
# while(num!=0):
#     r=num%10
#     if r%2==0:
#         sumeven=sumeven+r
#     else:
#         oddeven=oddeven+r
#     num=num//10
#
#
# print(sumeven)
# print(oddeven)
#
# a=10
# b=20
#
# a=10+10
# print(a)
#
# b=a-10
# print(b)