def is_palindrome():
    given_string = str(input())
    return given_string == given_string[::-1]


if __name__ == '__main__':
    print(is_palindrome())
