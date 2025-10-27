# # note:method name shoud be same
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
#     def carry(self):
#         print("plane is cayying the passengers")
#
#
# class cargo(plane):
#     def __init__(self):
#         super().__init__()
#
#     def carry(self):
#             print("plane is cayying the goods")
#
#
# class fighter(plane):
#     def __init__(self):
#         super().__init__()
#
#     def carry(self):
#         print("plane is cayying the weapons ")
#
#
#
#
# f1=fighter()
# c1=cargo()
# p1=passenger()
#
# def helloplane(par):
#     par.takeoff()
#     par.flying()
#     par.landing()
#     par.carry()
#     par.carry()
#     par.carry()
#
# helloplane(f1)
#












class Bird:
    def move(self):
        return "I fly!"

class Penguin(Bird):
    def move(self):   # overriding
        return "I waddle!"

b1 = Bird()
b2 = Penguin()

print(b1.move())   # I fly!
print(b2.move())   # I waddle!
