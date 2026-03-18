def topkfrequent(numbers, k):
    count = {}
    for n in numbers:
        if n not in count:
            count[n] = 1
        else:
            count[n] += 1

    items = []
    for numbers in count:
        items.append([numbers, count[numbers]])

    items.sort(key=lambda a: (-a[1], a[0]))

    result = []
    for i in range(k):
        result.append(items[i][0])

    return result

numbers = [1, 1, 1, 2, 2, 3]
k = 2
print(topkfrequent(numbers, k))

numbers = [4, 4, 4, 6, 6, 1, 1, 1, 1, 2]
k = 2
print(topkfrequent(numbers, k))
