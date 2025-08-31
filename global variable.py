# a=10
#
# def fun1():
#     a=100
#     b=200
#     print(a)
#     print(b)
#
# def fun2():
#     c=300
#     print(a)           #global variable
#     print(c)
#
#
# fun1()
# fun2()
#



#modification of a global variable

a=10

def fun1():
    global a         #print a as global variable
    a=100
    b=200
    print(a)
    print(b)

def fun2():
    global a          #print a as global variable (converting local variable into global varible)
    a=150
    b=250
    print(a)           #global variable
    print(b)

print(a)
fun1()
print(a)
fun2()
print(a)