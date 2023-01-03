# Universe was created after this:
import time

# It just describes post
class Post:
    # Init...
    def __init__(self, user, title, content):
        self.user = user
        self.title = title
        self.content = content
        self.timestamp = time.time()

    # Returns title
    def get_title(self):
        return self.title

    # Returns content
    def get_content(self):
        return self.content

    # Returns timestamp
    def get_timestamp(self):
        return self.timestamp
    
    # Returns user's name
    def get_user(self):
        return self.user.get_name()

