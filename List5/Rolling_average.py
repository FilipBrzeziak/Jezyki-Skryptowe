def rolling_average():
    numbers = [2, 1, 5, 7.7, 12]
    step_size = numbers[0]
    rolling_averages = []
    i = 1
    while i < len(numbers) - step_size + 1:
        step = numbers[i: i + step_size]
        step_average = sum(step) / step_size
        rolling_averages.append(step_average)
        i = i + 1

    return rolling_averages


if __name__ == '__main__':
    print(rolling_average())
