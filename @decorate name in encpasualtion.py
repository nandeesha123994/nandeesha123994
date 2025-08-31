class person:
    def __init__(self):
        self.__name="manu"


    @property
    def displayname(self):
        return self.__name
    @displayname.setter

    def displayname(self,val):
        self.__name=val


p1=person()
p1.displayname='nandi'
res=p1.displayname
print(res)