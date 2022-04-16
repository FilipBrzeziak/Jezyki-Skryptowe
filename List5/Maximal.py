import sys


def maximal():
    i = -sys.maxsize - 1
    numbers = list(map(int, str.split(input(), " ")))

    for number in numbers:
        if int(number) > i:
            i = int(number)

    return i


if __name__ == '__main__':
    print(maximal())
