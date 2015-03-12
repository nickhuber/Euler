# Start at 100, need at least 6 combinations
i = 99
while True:
    i += 1
    results = set()
    for potential in range(2, 7):
        results.add(''.join(sorted(str(i * potential))))
        if len(results) != 1:
            break
    if len(results) != 1:
        continue
    print(i)
    quit()
