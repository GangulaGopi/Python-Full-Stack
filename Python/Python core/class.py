# class Profile:
#     def __init__(self,username):
#         self.followers=0
#         self.username=username
#     def follow(self):
#         print("someone followed you")
#         self.followers+=1
#     def update_username(self,user):
#         print("New user is created")
#         self.username=user
# P1=Profile("_manikanta_143-")
# P1.follow()
# print(P1.followers)
# P1.update_username("mani")
# print(P1.username)
#

# class Person:
#     total_no_of_phones=0
#     def __init__(self,name,age,phone):
#         self.name=name
#         self.age=age
#         self.phone=phone
#         if phone:
#             Person.total_no_of_phones+=1
# p1=Person("gopi",22,True)
# p2=Person("praneeth",22,False)



# class Building:
#     no_of_rooms =10
#     total_count=0
#     def __init__(self, name, wifi):
#         self.building_name=name
#         self.wifi=wifi
#         Building.total_count+=1
#     def change_rooms(self,nor):
#         Building.no_of_rooms=nor
# b1=Building("New Building",True)
# print(b1.total_count)
# b2=Building("New2 Building",False)
# print(b2.total_count)

class Bank:
    Bank_name="CVBank"
    def __init__(self,name,balance):
        self.holder=name
        self.balance=balance
    @classmethod
    def change_Bank_name(cls,new):
        cls.Bank_name=new
    def deposit(self,amount):
        self.balance+=amount
    @staticmethod
    def validate(amount):
        return amount>0

b1=Bank("gopi",10000000)
b1.change_Bank_name("SBI")
b1.deposit(20000000)
b2=Bank("mani",20000000)
print(b1.validate(1000))
print(b2.validate(20000000))