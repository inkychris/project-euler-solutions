def sum_even_fibonacci(n_max):
    fib_n_1 = 0
    fib_n = 1
    sum = 0

    while True:
        new_fib = fib_n_1 + fib_n

        if new_fib >j n_max:
            break

        fib_n_1 = fib_n
        fib_n = new_fib

        if fib_n % 2 == 0:
            sum += fib_n

    return sum

print(sum_even_fibonacci(3999999))
