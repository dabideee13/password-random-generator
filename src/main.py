import string
from random import choice

ALL = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation


def generate_password(password_length: int) -> str:
    return "".join(choice(ALL) for _ in range(password_length))


def main():
    print(generate_password(16))


if __name__ == "__main__":
    main()
