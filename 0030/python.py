def problem_30():
    found = 0
    for i in range(2, 6 * 9 ** 5):
        numbers = str(i)
        summed = sum(map(lambda x: int(x) ** 5, numbers))
        if summed == i:
            found += i
    return found

if __name__ == '__main__':
    print(problem_30())
