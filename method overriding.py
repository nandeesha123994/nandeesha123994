class A:
    def disp(self):
        print("display a")

class B(A):
    def disp(self):
        print("display b")

class C(B):
    def disp(self):
        print("display c")

c1=C()

c1.disp()
c1.disp()
c1.disp()