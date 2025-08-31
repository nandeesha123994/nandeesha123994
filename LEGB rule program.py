# a=10                #golbal
#
# def fun1():
#     #a=20           #enclosed
#     def fun2():
#         #a=30         #local
#         print(a)
#
#     fun2()
#
# fun1()


#eg on built in space

from math import pi

#pi=10                #golbal

def fun1():
    #pi=20           #enclosed
    def fun2():
        #pi=30         #local
        print(pi)

    fun2()

fun1()


