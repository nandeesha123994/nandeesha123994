# class book:
#     def __init__(self,page):
#         self.__pages=page       #private varaible
#
#
#
# b1=book(100)
# print(b1.__pages)             #accesing the ouside the class it will thorugh an error



# class book:
#     def __init__(self,page):
#         self.__pages=page                                 #private variable
#
#     def setter(self,val):
#         if val>0:
#             self.__pages=val                               #assigning the value
#     def getter(self):
#         return self.__pages                               # returning the private value
#
#
# b1=book(100)
# res1=b1.getter()                                          #accesing the private variable outside of the class
# print(res1)       #100
# b1.setter(200)
# res2=b1.getter()
# print(res2)        #200
# b1.setter(-99)     #condition become false
# res3=b1.getter()
# print(res3)         #300














# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance   # private variable
#
#     # Getter
#     def get_balance(self):
#         return self.__balance
#
#     # Setter
#     def set_balance(self, amount):
#         if amount >= 0:
#             self.__balance = amount
#         else:
#             print("Invalid amount")
#
# # Usage
# acc = BankAccount(1000)
# print(acc.get_balance())   # ✅ Access via getter
# acc.set_balance(2000)      # ✅ Update via setter
# print(acc.get_balance())
# acc.set_balance(-500)      # ❌ Invalid



class person:
    def __init__(self):
        self.__name="manu"
    def setter(self,val):
        self.__name=val
    def getter(self):
        return self.__name

p1=person()
p1.setter('nandi')
res=p1.getter()
print(res)