from user import User
from post import Post

def print_post(post: Post) -> None:
    print(f'Title: {post.get_title()}')
    print(f'Content: {post.get_content()}')
    print(f'Author: {post.get_user()}')
    print(f'Timestamp: {post.get_timestamp()}')

def main() -> None:
    user = User('John', 30)
    post = user.create_post('Hello World', 'This is my first post')
    print_post(post)

main()

