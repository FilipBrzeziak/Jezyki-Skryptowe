def average():
    numbers = list(map(float, str.split(input(), " ")))
    i = 0

    for number in numbers:
        i = i + number

    return i / len(numbers)


if __name__ == '__main__':
    print(average())
