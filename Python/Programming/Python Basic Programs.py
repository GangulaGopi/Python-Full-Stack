# # # a=int(input())
# # # b=int(input())
# # # c=(a+b)
# # # print(c)
# # n=int(input())
# # fc=0
# # if n==0:
# #     print("Invalid Input")
# # else:
# #     n=abs(n)
# #     for i in range(1,n+1):
# #         if n%i==0:
# #             fc+=1
# #     if fc==2:
# #         print("prime")
# #     else:
# #         print("Not a prime")
#
# n=int(input())
# fc=0
# if n==0:
#     print("Invalid Input")
# else:
#     n=abs(n)
#     i = 2
#     while i <= n:
#         if n % i == 0:
#             print(i)
#             n = n // i
#         else:
#             i += 1
#
#
# def is_prime(num):
#     fc=0
#     for i in range(1,num+1):
#         if num%i==0:
#             fc+=1
#         if fc==2:
#             return True
#         else:
#             return False
n=int(input())
n1=int(input())
c=0
b=False
for i in range(n,n1+1):
    fc=0
    for j in range(1,i+1):
        if i%j==0:
            fc+=1
    if fc==2:
        print(i,end=" ")
        b=True
if b==False:
    print("no prime")