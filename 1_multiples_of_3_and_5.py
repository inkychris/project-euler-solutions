def sum_multiples(a, b):
    sum = 0
    for i in range(a, b + 1):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum

print(sum_multiples(1, 999))
