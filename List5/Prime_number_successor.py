def is_prime(number):
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False
    return True


def find_succesor(number):
    number = number + 1
    while not is_prime(number):
        number = number + 1
    return number


if __name__ == '__main__':
    print(find_succesor(int(input("Number:"))))
