class demo:
    def disp(self,a=10,b=20,c=30):  #default arguments
        print(a)
        print(b)
        print(c)

d1=demo()
x=23
y=34
z=28
d1.disp()
d1.disp(x)
d1.disp(y)
d1.disp(x,y)
d1.disp(c=z)  #keyword arguments
d1.disp(a=z)

