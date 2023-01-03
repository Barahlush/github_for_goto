# Wow import user from user...
from user import User

# It prints post! Amazing
def print_post(post):
    print(f'Title: {post.get_title()}')
    print(f'Content: {post.get_content()}')
    print(f'Author: {post.get_user()}')
    print(f'Timestamp: {post.get_timestamp()}')

# Just main void that creates new user John (he's 30 y.o) and prints he's first post (Hello world!)
def main():
    user = User('John', 30)
    post = user.create_post('Hello World', 'This is my first post')
    print_post(post)

main()

