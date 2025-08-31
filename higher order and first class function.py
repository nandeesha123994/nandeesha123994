def fun1():
    print("fun1 is calling")

def fun2(ref):              #higher order function(the function accepting another function is cld)
    print("fun2 is calling")
    ref()


fun1()
fun2(fun1)