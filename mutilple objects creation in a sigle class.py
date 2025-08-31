#multiple object creation in single class
class student:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id


s1=student('nandi',12,123)  #multiple object creation
s2=student('kali',45,345)

print(s1.id,s1.name,s1.age)
print(s1.age)
print(s1.id)