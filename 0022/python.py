import string


def get_name_score(name):
    return sum(map(lambda c: string.uppercase.index(c) + 1, name))


def problem_22():
    with open('p022_names.txt', 'r') as f:
        content = f.read()

    # Remove the " characters from the data set
    content = content.replace('"', '')
    names = content.split(',')
    names.sort()

    score = 0
    for index, name in enumerate(names, start=1):
        score += get_name_score(name) * index
    return score


if __name__ == '__main__':
    print(problem_22())
