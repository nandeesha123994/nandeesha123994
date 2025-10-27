# class parentclass:
#     def __init__(self):
#         self.a=10
#
# class childclass(parentclass):                       #connecting the two classes
#     def __init__(self):
#         parentclass.__init__(self)                  #connecting the two constructers
#         self.b=20
#
# c1=childclass()
# print(c1.a)
# print(c1.b)



# #using the three classes
#
# class A:
#     def __init__(self):
#         self.a=10
#
# class B(A):
#     def __init__(self):
#         A.__init__(self)
#         self.b=20
#
# class C(B):
#     def __init__(self):
#         B.__init__(self)
#         self.c=30
#
#
# c1=C()
# b1=B()
# print(c1.c)
# print(c1.b)
# print(c1.a)
# print(b1.a)
# print(b1.b)

#invoking the parent class constrocter mannually

# class A:
#     def __init__(self):
#         self.a=10
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.b=20
#
# class C(B):
#     def __init__(self):
#         super().__init__()
#         self.c=30
#
#
# c1=C()
# print(c1.c)
# print(c1.b)
# print(c1.a)




#
# class plane:
#
#
#     def takeoff(self):
#             print("plane is takeoff")
#
#     def flying(self):
#             print("plane is flying")
#
#     def landing(self):
#             print("plane is landing")
#
# class passenger(plane):
#     def __init__(self):
#         super().__init__()
#
#     def carry_p(self):
#         print("plane is cayying the passengers")
#
#
# class cargo(plane):
#     def __init__(self):
#         super().__init__()
#
#     def carry_g(self):
#             print("plane is cayying the goods")
#
#
# class fighter(plane):
#     def __init__(self):
#         super().__init__()
#
#     def carry_w(self):
#         print("plane is cayying the weapons ")
#
#
#
#
# f1=fighter()
# c1=cargo()
# p1=passenger()
#
# c1.carry_g()
# c1.takeoff()
# c1.landing()
#
# p1.carry_p()
# p1.takeoff()
# p1.landing()
#
# f1.carry_w()
# f1.takeoff()
# f1.landing()


# class animal:
#         def eat(self):
#             print("eating")
#         def sleep(self):
#             print("sleeping")
#         def hunt(self):
#             print("hunting")
#
#
# class tiger(animal):
#     pass
# class  hyna(animal):
#     pass
#
# class monkey(animal):
#     pass
#
#
# t1=tiger()
# h1=hyna()
# m1=monkey()
#
# t1.eat()
# t1.sleep()
# t1.hunt()
#
# h1.eat()
# h1.sleep()
# h1.hunt()
#
# m1.eat()
# m1.sleep()
# m1.hunt()






























