class Profile:
    def __init__(self,username):
        self.followers=0
        self.username=username
    def follow(self):
        print("someone followed you")
        self.followers+=1
    def update_username(self,user):
        print("New user is created")
        self.username=user
P1=Profile(" _manikanta_143-")
P1.follow()
print(P1.followers)
P1.update_username("mani")
print(P1.username)
