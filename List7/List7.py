from timeit import default_timer as timer
import re

all_cases = []
by_date = {}
by_country = {}

# Task 1
with open(r'Covid.txt', 'r', encoding="utf8") as f:
    f.readline()
    lines = f.readlines()
    for line in lines:
        line = line.split('\t')
        all_cases.append((line[0], line[6], line[5], line[4]))

        if line[0] in by_date.keys():
            by_date[line[0]].append((line[6], int(line[5]), int(line[4])))
        else:
            by_date[line[0]] = [(line[6], int(line[5]), int(line[4]))]

        if line[6] in by_country:
            by_country[line[6]].append((line[0], int(line[5]), int(line[4])))
        else:
            by_country[line[6]] = [(line[0], int(line[5]), int(line[4]))]


# Task 2
def for_date_a(date):
    deaths = 0
    cases = 0
    for entry in all_cases:
        if date == entry[0]:
            deaths += int(entry[2])
            cases += int(entry[3])

    return deaths, cases


def for_date_d(date):
    deaths = 0
    cases = 0
    for entry in by_date[date]:
        deaths += int(entry[1])
        cases += int(entry[2])

    return deaths, cases


def for_date_c(date):
    deaths = 0
    cases = 0
    for dates in by_country.values():
        for entry in dates:
            if date == entry[0]:
                deaths += int(entry[1])
                cases += int(entry[2])
    return deaths, cases


# Task 3
def for_country_a(country):
    deaths = 0
    cases = 0
    for entry in all_cases:
        if country == entry[1]:
            deaths += int(entry[2])
            cases += int(entry[3])

    return deaths, cases


def for_country_d(country):
    deaths = 0
    cases = 0
    for dates in by_date.values():
        for entry in dates:
            if country == entry[0]:
                deaths += int(entry[1])
                cases += int(entry[2])

    return deaths, cases


def for_country_c(country):
    deaths = 0
    cases = 0
    for entry in by_country[country]:
        deaths += int(entry[1])
        cases += int(entry[2])
    return deaths, cases


def measure_time(func, *args):
    start = timer()
    result = func(*args)
    end = timer()
    return result, (end - start) * 1000


# Task 4

def valid_email(email):
    if re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[pwr]+\.[edu]+\.[pl]{2,}\b', email):
        name = str(re.split("@", email, maxsplit=1)[0])
        return name
    else:
        return "None"


def valid_number(phone_nuber):
    if (re.fullmatch(r'^[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{3}', phone_nuber)) or (
            re.fullmatch(r'[\dA-Z]{3} [\dA-Z]{3} [\dA-Z]{3}', phone_nuber)) or (
            re.fullmatch(r'[+]48+[ ]+[\dA-Z]{9}', phone_nuber)) or (
            re.fullmatch(r'[+]48+[ ]+[\dA-Z]{3} [\dA-Z]{3} [\dA-Z]{3}', phone_nuber)):
        return True
    else:
        return False


if __name__ == '__main__':
    task2 = [measure_time(for_date_a, "30.04.2020"), measure_time(for_date_d, "30.04.2020"),
             measure_time(for_date_c, "30.04.2020")]

    print("Task 2:")

    for entry in task2:
        print('Deaths: {0:>8d}      cases: {1:>9d}       execution time: {2:>20f}'.format(entry[0][0], entry[0][1],
                                                                                          entry[1]))

    task3 = [measure_time(for_country_a, 'Albania'), measure_time(for_country_d, 'Albania'),
             measure_time(for_country_c, 'Albania')]

    print("\nTask 3:")

    for entry in task3:
        print('Deaths: {0:>8d}      cases: {1:>9d}       execution time: {2:>20f}'.format(entry[0][0], entry[0][1],
                                                                                          entry[1]))

    print("\nTask 4:")

    print("\nEmail test:")
    print(valid_email('12345@pwr.edu.pl'))
    print(valid_email('12345@gmail.com'))
    print("\nNumber test:")
    print(valid_number('+48 567 898 567'))
    print(valid_number('+48 567898567'))
