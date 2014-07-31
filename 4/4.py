def is_palindrome(s):
    return s == s[::-1]

largest = None
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if product > largest and is_palindrome(str(product)):
            largest = product
        j += 1
    i += 1

print(largest)

