class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0  # instead of asigning parameters to the attribute, we can assign a constant values as well

    def increase_follower(self):
        print(self.followers)
        self.followers = self.followers + 1
        print(self.followers)

user_1 = User("0001", "Nirav" )
print(user_1.username)
print(user_1.id)
user_2 = User("0002", "Manya")
print(user_2.username)
print(user_2.id)
print(user_1.increase_follower())