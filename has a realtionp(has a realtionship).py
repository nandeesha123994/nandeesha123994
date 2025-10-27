# class Radio:
#     def turnOn(self,a):
#         if a==1:
#             print("radio is on")
#         else:
#             print("radio is off")
#
#
# class Car:
#     def __init__(self,min,max):
#         self.min=min
#         self.max=max
#         self.r=Radio()
#
# c1=Car(10,20)
# print(c1.min)
# print(c1.max)
# c1.r.turnOn(1)
# c1.r.turnOn(0
#             )



# implemetation of composed object
#note: without mobile(main object) os is not exited

# class os:
#     def __init__(self):
#         self.status=True
#         print("os is ready")
#
#     def getos(self):
#         print("os is installing")
#
#
#
# class mobile:
#     def __init__(self,name):
#         self.mname=name
#         self.o=os()                          #object creation
#         print("mobile is ready")
#         print("with os is installed")
#
# m1=mobile("nokia")
# print(m1.o.status)
# m1.o.getos()
# del m1                                         #deleting the main object
# print(m1.o.status)                             #accesing the os variable (composed oject)
#
# #implementaion of aggregate object

# class charger:
#     def __init__(self,name):
#         self.cname=name
#
#     def getcharger(self):
#         print("mobile is charging")
#
# class mobile:
#     def __init__(self,name):
#         self.mname=name
#         self.c=""
#
#     def hasmobile(self,p):
#         self.c=p
#
# m1=mobile("karbon")
# c1=charger("type c")
# m1.hasmobile(c1)
#
# print(m1.c.cname)
# m1.c.getcharger()
#
# del m1
# print(c1.cname)
#


#combination of both composed object anf aggregate object
class brian:                                                              #composed object
    def __init__(self):
        self.status="active"

    def getbrian(self):
        print("brian is working")


class person:                                                             #main object

    def __init__(self,name):
        self.pname=name
        self.b=brian()                                                    #creating the object for composed object
        self.c=""
    def hascar(self,p):
        self.c=p

class car:                                                    #composed object
    def __init__(self,name):
        self.cname=name

    def getcar(self):
        print("getting a car")

p1=person("nandi")
c1=car("maruthi")

print(p1.b.status)                                        #printing the status of brian     #composed object
p1.b.getbrian()                                           #calling the getbrian             #composed object
print(p1.pname)                                           #printing the pname of person     #main object
p1.hascar(c1)                                             #calling the main object
print(p1.c.cname)                                         #aggregate object
p1.c.getcar()                                             #aggregate object

del p1                                                    #deleting the main object
# print(p1.b.status)                                      #accesing the composed object it will give error
print(c1.cname)                                          #accesing the aggegate object it will give the output























