def problem_29():
    results = set()
    for a in range(2, 101):
        for b in range(2, 101):
            results.add(a ** b)
    return len(results)


if __name__ == '__main__':
    print(problem_29())
