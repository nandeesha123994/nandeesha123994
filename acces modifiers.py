

#public

# class Student:
#     def __init__(self, name):
#         self.name = name   # public variable
#
# obj = Student("Nanda")
# print(obj.name)   # ✅ Accessible

#private

# class Student:
#     def __init__(self, name):
#         self._name = name   # public variable
#
# obj = Student("Nanda")
# print(obj._name)   # ✅ Accessible

#using the method we can acess the private variable outside the class
class Student:
    def __init__(self, name):
        self.__name = name   # private variable

    def display(self):  # private method
        return self.__name
        #print("Name:", self.__name)


obj = Student("Nanda")
res=obj.display() # ✅ Accessible via method
print(res)
obj.res='kali'     # modifing the private variable outside the class
print(obj.res)
# print(obj.__name)    # ❌ Error
print(obj._Student__name)  # ⚠️ Possible but not recommended



