def fun1():
    print("fun1")

    def fun2():
        print("fun2")

    return fun2

res=fun1()
res()


