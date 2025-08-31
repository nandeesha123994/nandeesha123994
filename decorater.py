def main():
    print("main")

def outer(ptr):                                            #storing the main=ptr
    print("outer function")

    def inner():
        print("inner function")
        ptr1=ptr                                             #copying the main into pt1
        ptr1()
        print("after main function")
    return inner                                              #returning the addres the of inner function

res=outer(main)                                                #stririn the inner addres into the res variable
res()                                                          #closure function