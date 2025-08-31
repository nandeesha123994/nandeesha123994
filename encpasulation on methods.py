class car:
    def __init__(self):
        self.color="black"

    def __move(self):                                   #converting the public method into private method
        print("car is moving")

    def helper(self):                                   #passing the private mthod inside anthoer method
        self.__move()

    # def cohelper(self):
    #     self.helper()

c1=car()
c1.helper()                                             #