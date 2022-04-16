import pandas as pd
from sys import argv

import Levenshtein


def covid_sum():
    country = argv[1]
    similarity_level = int(argv[2])
    data = pd.read_csv('Covid.txt', sep='\t')
    countries = []
    for index, row in data.iterrows():
        if Levenshtein.levenshtein_in_distance(row[6], country) <= similarity_level:
            countries.append(row[6])

    def sorter(this):
        return Levenshtein.levenshtein_in_distance(this, country)

    countries.sort(reverse=True, key=sorter)
    return countries


if __name__ == '__main__':
    print(covid_sum())
