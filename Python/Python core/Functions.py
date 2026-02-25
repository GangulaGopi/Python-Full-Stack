def is_prime(x):
    fc=0
    for i in range(1,x+1):
        if x%i==0:
            fc+=1
    if fc==2:
        return x
    return False
r=is_prime(1)
print(r)
a=int(input())
b=int(input())
for i in range(a,b+1):
    if is_prime(i):
        print(i)
