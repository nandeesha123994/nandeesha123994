# a=int(input("enter the vlaue of a"))
# b=int(input("enter the vlaue of b"))
#
# res=a/b
# print(res)


# a=int(input("enter the vlaue of a"))
# b=int(input("enter the vlaue of b"))
#
# try:
#     res=a/b
#     print(res)
#
# except Exception as e:
#     print("erorr occured")


# def fun1():
#     print("entering fun1")
#
#     try:
#         fun2()
#     except Exception as e:
#         print("error occured fun1")
#     print("leaving fun1")
#
# def fun2():
#     print("entering fun2")
#     res=10/0
#     print(res)
#     print("leaving fun2")
#
# print("pgm started")
# fun1()
# print("pgm end")
#
#



#RAISE KEYWORD(withou raise keyword)

# def fun1():
#     print("entering fun1")
#     try:
#         fun2()
#     except Exception as e:
#         print("error occured in fun1")
#
#     print("leaving fun1")
#
# def fun2():
#     print("wntering fun2")
#
#     try:
#         res=10/0
#         print(res)
#     except Exception as e:
#         print(" error occured in fun2")
#     print("laeving fun2")
#
# print("program started")
# fun1()
# print("program ended")










#RAISE KEYWORD(with raise keyword)

# def fun1():
#     print("entering fun1")
#     try:
#         fun2()
#     except Exception as e:
#         print("error occured in fun1")
#
#     print("leaving fun1")

# def fun2():
#      print("wntering fun2")
#
#     try:
#         res=10/0
#         print(res)
#     except Exception as e:
#         print(" error occured in fun2")
#         raise e
#     print("laeving fun2")
#
# print("program started")
# fun1()
# print("program ended")



#finaaly block


# def fun1():
#     print("entering fun1")
#     try:
#         fun2()
#     except Exception as e:
#         print("error occured in fun1")
#
#     print("leaving fun1")
#
# def fun2():
#     print("wntering fun2")
#
#     try:
#         res=10/0
#         print(res)
#     except Exception as e:
#         print(" error occured in fun2")
#         raise e
#     finally:
#         print("laeving fun2")
#
# print("program started")
# fun1()
# print("program ended")


#ELSE BLOCK

# a=int(input("enter value a"))
# b=int(input("enter a value of b"))
#
# try:
#     res=a/b
#     print(res)
#
# except Exception as e:
#     print("eorr is occured")
#
# else:
#     print("prgram run suseefully")
#


#handling all execeptions


# try:
#     a=int(input("enter the vlaue of a"))
#     b=int(input("enter the vlaue of b"))
#
#     res=a/b
#     print(res)
#
# except ValueError as e:
#      print("vlaue eoor")
# except ZeroDivisionError as e:
#     print("zero divsion error")
# except Exception as e:
#     print("error occured")
#


#in one block handling multiple values

# try:
#     a=int(input("enter the vlaue of a"))
#     b=int(input("enter the vlaue of b"))
#
#     res=a/b
#     print(res)
#
# except (ValueError,ZeroDivisionError) as e:
#      print("vlaue eoor or zero division error")
#
# except Exception as e:
#     print("error occured")



#printing the error m esage defaulty

try:
    a=int(input("enter the vlaue of a"))
    b=int(input("enter the vlaue of b"))

    res=a/b
    print(res)


except Exception as e:
    print("error occured")
    print(e.__str__())          #cheking thwe error
    print(e)                     #we can also use this one
















