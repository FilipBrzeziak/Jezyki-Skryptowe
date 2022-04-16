import Prime_number_successor


def find_k_succesors():
    succesors = []
    number = int(input("Number:"))
    k = int(input("K:"))
    for i in range(k):
        number = Prime_number_successor.find_succesor(number)
        succesors.append(number)
    return succesors


if __name__ == '__main__':
    print(find_k_succesors())
