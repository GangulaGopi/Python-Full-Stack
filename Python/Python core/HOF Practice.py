# # # # # n=[[1, 2], [3, 4], [5, 6]]
# # # # # m=list(map(lambda x: x.append(5),n))
# # # # # print(m)
# # # # # n = [[1, 2], [3, 4], [5, 6]]
# # # # # result = list(map(lambda x: x+[5], n))
# # # # # print(result)
# # # #
# # # # d = {"apple": 100, "banana": 40, "cherry": 150}
# # # # r=dict(filter(lambda i:i[1]>50,d.items()))
# # # # print(r)
# # # from functools import reduce
# # # l=[20,10,5,6,8]
# # # r=max(l)
# # # print(r)
# # # r=reduce(lambda a,b : a if a>b  else b,l)
# # # print(r)
# #
# # s=("gopi")
# # r=list(map(lambda x: ord(x),s))
# # print(r)
# #
# # s=("gopi123")
# # r=list(map(lambda x: ord(x),s))
# # print(r)
# #
#
# # t=("AEIOUaeiou")
# # r=list(filter(lambda x:x not in t,input() ))
# # print(r)
# from functools import reduce
# l=['P', 'y', 't', 'h', 'o', 'n']
# r= reduce(lambda a,b:a+b,l)
# print(r)
#For print object adress
# l=[10]
# k=(map(lambda x:x,l))
# print(k)
# # to print object id
# l=[10]
# r=list((map(lambda x: id(x),l)))
# print(r)
from functools import reduce
#
# s=[5, 10, 15, 20, 25, 30]
# r=reduce(lambda a,b:a+b,
#          filter(lambda x:x%5==0,
#                 map(lambda x: x**2,s)
#          )
# )
# print(r)

s=[5, 10, 15, 20, 25, 30]
r=reduce(lambda a,b:a+b,filter(lambda x:x%5==0,map(lambda x: x**2,s)))
print(r)