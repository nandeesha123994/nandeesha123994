# def generator():
#     yield 1
#     yield 2
#     yield 3
#
#
#
# res=generator()
# print(res)


# def generator():
#     yield 1
#     yield 2
#     yield 3
#
# res=generator()
# print(next(res))
# print(next(res))
# print(next(res))


#comparision of generstor and return

# def numbers():
#     for i in range(1,10001):
#         yield i
# res=numbers()
# print(next(res))
# print(next(res))
# print(next(res))


def numbers():
    return [i for i in range(1,1001)]

res=numbers()

print(res)


















