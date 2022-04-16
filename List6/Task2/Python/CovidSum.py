import pandas as pd
from sys import argv


def covid_sum():
    covid_cases = 0
    country = argv[1]
    month = int(argv[2])
    data = pd.read_csv('Covid.txt', sep='\t')
    for index, row in data.iterrows():
        if month == int(row[2]) and (country == row[6]):
            covid_cases = covid_cases + row[4]

    return covid_cases


if __name__ == '__main__':
    print(covid_sum())
