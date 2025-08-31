# def fun1():
#     a=10
#     b=20
#     print(a)
#     print(b)
#     def fun2():
#         c=30
#         print(c)
#         def fun3():
#             d=40
#             fun3()
#             print(d)
#
#         fun3()
#     fun2()
#
# fun1()


#aceesing and modifying the non local varaible


def outer():
    a=10
    b=20
    print(a)
    print(b)
    def inner():
        nonlocal a
        a=100
        c=300
        print(a)
        print(c)
    print(a)            #10
    inner()
    print(a)  #100

outer()
