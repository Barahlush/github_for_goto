import time


class Post:
    def __init__(self, user, title, content):
        self.user = user
        self.title = title
        self.content = content
        self.timestamp = time.time()

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_timestamp(self):
        return self.timestamp

    def get_user(self):
        return self.user.get_name()
