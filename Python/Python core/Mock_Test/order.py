from functools import reduce

s=[1,2,6,5,2,3,8,9,12]
r=reduce(lambda x,y:x+y,filter(lambda x:x%7==0,map(lambda x: x**3,s)),0)
print(r)
