# # # # a=int(input())
# # # # b=int(input())
# # # # c=(a+b)
# # # # print(c)
# # # n=int(input())
# # # fc=0
# # # if n==0:
# # #     print("Invalid Input")
# # # else:
# # #     n=abs(n)
# # #     for i in range(1,n+1):
# # #         if n%i==0:
# # #             fc+=1
# # #     if fc==2:
# # #         print("prime")
# # #     else:
# # #         print("Not a prime")
# #
# # n=int(input())
# # fc=0
# # if n==0:
# #     print("Invalid Input")
# # else:
# #     n=abs(n)
# #     i = 2
# #     while i <= n:
# #         if n % i == 0:
# #             print(i)
# #             n = n // i
# #         else:
# #             i += 1
# #
# #
# # def is_prime(num):
# #     fc=0
# #     for i in range(1,num+1):
# #         if num%i==0:
# #             fc+=1
# #         if fc==2:
# #             return True
# #         else:
# #             return False
# n=int(input())
# n1=int(input())
# c=0
# b=False
# for i in range(n,n1+1):
#     fc=0
#     for j in range(1,i+1):
#         if i%j==0:
#             fc+=1
#     if fc==2:
#         print(i,end=" ")
#         b=True
# if b==False:
#     print("no prime")
#Day 1
#sum of digits
# n=int(input())
# sum=0
# while n>0:
#     r=n%10
#     sum+=r
#     n=n//10
# print(sum)
#even or odd
# n=int(input())
# if n%2==0:
#     print("Even Number")
# else:
#     print("Odd Number")
#prime Number
# n=int(input())
# fc=0
# for i in range(1,n+1):
#     if n%i==0:
#         fc+=1
# if fc==2:
#     print("Prime Number")
# else:
#     print("Not a prime number")
#factors of a given number
# n=int(input())
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
# factor count
# n=int(input())
# fc=0
# for i in range(1,n+1):
#     if n%i==0:
#         fc+=1
# print(fc)
# factorial of a number
# n=int(input())
# fc=1
# for i in range(1,n+1):
#     fc=fc*i
# print(fc)

#reverse a number
# n=int(input())
# rev=0
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n=n//10
#     print(r,end="")
#Day 2
# student grading system
A=0
B=0
C=0
D=0
E=0
F=0
for i in range(7):
    n=int(input())
    if n>90:
        A+=1
    elif n>80:
        B+=1
    elif n>70:
        C+=1
    elif n>60:
        D+=1
    elif n>40:
        E+=1
    else:
        F+=1
maximum=max(A,B,C,D,E,F)
if maximum==A:
    print("A")
elif maximum==B:
    print("B")
elif maximum==C:
    print("C")
elif maximum==D:
    print("D")
elif maximum==E:
    print("E")
elif (maximum==F):
    print("F")