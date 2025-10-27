# class student:
#
#     def sum(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#           s=a+b+c
#           return s
#         elif a!=None and b!=None:
#             s=a+b
#             return s
#         else:
#             s=a
#             return  s
# s1=student()
#
# res=s1.sum(1)
# print(res)
#




#using default argument

# class Math:
#     def add(self, a=0, b=0, c=0):
#         return a + b + c
#
# m = Math()
# print(m.add(2, 3))       # 5
# print(m.add(2, 3, 4))    # 9


class A:
    def disp(self,a):
        print(a)

class B(A):
    def disp(self,a,b):
        print(a)
        print(b)

class C(B):
    def disp(self,a,b,c):
        print(a)
        print(b)
        print(c)


c1=C()
c1.disp(10,20,30)
c1.disp(10,20)
c1.disp(10)