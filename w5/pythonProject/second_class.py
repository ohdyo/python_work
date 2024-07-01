class User:
    def __init__(self,id,name):
        self.id = id
        self.userName = name
        self.following = 0
        self.follower = 0
    def follow(self,user):
        self.following += 1
        user.follower += 1

user_1 = User("001","pica")
print(user_1.userName)

user_2 = User("002","kobu")
print(user_2.userName)


user_1.follow(user_2)
print(user_1.following)
print(user_2.following)
print(user_1.follower)
print(user_2.follower)

