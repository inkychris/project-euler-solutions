def reverse_number(n):
    return int(str(n)[::-1])

a = 0
b = 0
palendrome = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if product == reverse_number(product):
            if product > palendrome:
                a = i
                b = j
                palendrome = product

print(palendrome, a, b)
