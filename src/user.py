# Wow it's user
class User:
    # Just init again
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Returns user's name
    def get_name(self):
        return self.name

    # Returns user's age
    def get_age(self):
        return self.age

    # Creates post
    def create_post(self, title, content):
        return Post(self, title, content)
