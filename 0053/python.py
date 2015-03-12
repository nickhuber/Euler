max_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        max_sum = max(sum([int(i) for i in str(a ** b)]), max_sum)
print(max_sum)
