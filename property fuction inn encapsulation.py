class person:
    def __init__(self):
        self.__name="manu"

    def getter(self):
        return self.__name
    def setter(self,val):
        self.__name=val

    getset=property(getter,setter)

p1=person()
p1.getset='nandi'                              #using  getset assigning the vlaue
res=p1.getset                                  #using the getset calling the getset
print(res)                                      #printitng the value