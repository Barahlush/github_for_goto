from post import Post


class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age

    def create_post(self, title: str, content: str) -> Post:
        return Post(self, title, content)
