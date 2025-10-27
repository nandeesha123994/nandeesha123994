# t=(10,20,20)
# print(t)
# print(type(t))         #tuple
#
# t=(10)
# print(type(t))         #int
#
# t=(10,)
# print(type(t))         #tuple
#
# t=("nandi")
# print(type(t))         #str
#
# t=("nandi",)
# print(type(t))         #tuple
#
#

#indexing and slicing
#
# t=(10,20,30,40)
# print(t[-4:-1])
# print(t[-5: : ])


#cheking the immutal and mutable chRetr using the indeing na slicing

# l=[10,20,30]
# l[2]=200
# print(l)                #mutable
#
# l=(10,20,30)
# l[2]=200
# print(l)               #imutable


#insertion and deletion into a tuple

# t=(10,20,30,40)
# t1=t[ :1]+t[3:]
# print(t1)
#
# t2=t1[ :1]+(12,)+t1[1:]
# print(t2)


# names=["virat","dhoni","gayle","rohit"]
# j_num=[18,7,333,45]
# country=["ind","ind","west","ind"]
# ipl_team=["rcb","csk","punjab","mi"]
# res=list(zip(names,j_num,country,ipl_team))
# print(res)

#
# from itertools import zip_longest                                           #getting all the values using zip_longest
# names=["virat","dhoni","gayle","rohit"]
# j_num=[18,7,333,45]
# country=["ind","ind"]
# ipl_team=["rcb","csk","punjab","mi"]
# res=list(zip_longest(names,j_num,country,ipl_team))
# print(res)


from itertools import zip_longest                                           #fill value
names=["virat","dhoni","gayle","rohit"]
j_num=[18,7,333,45]
country=["ind","ind"]
ipl_team=["rcb","csk","punjab","mi"]
res=list(zip_longest(names,j_num,country,ipl_team,fillvalue="#"))
print(res)


