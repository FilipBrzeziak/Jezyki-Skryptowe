def levenshtein_in_distance(s, t):
    cols = len(t) + 1
    rows = len(s) + 1
    d = [[0 for x in range(cols)] for y in range(rows)]

    for i in range(rows):
        d[i][0] = i

    for j in range(cols):
        d[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):
            if s[i - 1] == t[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + cost)

    return d[rows - 1][cols - 1]


if __name__ == '__main__':
    print(levenshtein_in_distance('pies', 'pies'))
    print(levenshtein_in_distance('granat', 'granit'))
    print(levenshtein_in_distance('orczyk', 'oracz'))
    print(levenshtein_in_distance('marka', 'ariada'))
