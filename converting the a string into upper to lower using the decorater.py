def main():
    str='nandi'
    return str

def outer(ptr):                                            #storing the main=ptr
    print("outer function")

    def inner():
        print("inner function")
        res=ptr()                                             #calling the ptr(main function) and storing into the res variable
        ptr1=res.upper()                                      #converting the nandi into upper without affeting the main function
        print(ptr1)
    return inner                                              #returning the addres the of inner function

res=outer(main)                                                #stririn the inner addres into the res variable
res()