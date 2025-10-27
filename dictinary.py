# dict={"name":"nandi",
#        "age":19,
#         "add":"chintamani"
#       }
#
# print(dict)



#achiving deep copy in nested dictionary

import copy
heroine={"name":"samantha",
          "age":36,
          "bf":{"name1":"rahul",
                 "name2":"nehru"}
        }



print(heroine)
h1=heroine.copy()             #deep copy act as a shallow copy in a neste dictionary
h2=copy.deepcopy(heroine)     #deep copy
print("afetr")
print(heroine)
print(h1)
print(h2)
heroine['bf']['name3']="pavan"
print(heroine)
print(h1)
print(h2)




#zip function

# id=[101,102,103,104]
# name=['nagu','badhi','krisnha','rukmini']
# res1=dict(zip(id,name))
# print(res1)
# mob=[95,63,79,143]
# addr=['thailean','nigeria','russia','india']
# data=list(zip(name,mob,addr))
# info=dict(zip(id,data))
# print(info)