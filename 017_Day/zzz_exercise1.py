class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")
user_2 = User("002", "jack")

user_1.follow(user_2)
user_2.followers = user_2.followers + 100
print(user_1.id, " Followers: ", user_1.followers, " Following ", user_1.following)
print(user_2.id, " Followers: ", user_2.followers, " Following ", user_2.following)

