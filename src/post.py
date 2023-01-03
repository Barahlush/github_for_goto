import time
from user import User


class Post:
    def __init__(self, user: User, title: str, content: str):
        self.user = user
        self.title = title
        self.content = content
        self.timestamp = time.time()

    def get_title(self) -> str:
        return self.title

    def get_content(self) -> str:
        return self.content

    def get_timestamp(self) -> float:
        return self.timestamp
    
    def get_user(self) -> str:
        return self.user.get_name()

