def largest_prime_factor(n):
    prime_factors = []

    i = 2
    while n > 1:
        if n % i == 0:
            prime_factors.append(i)
            n /= i
            i = 2
        else:
            i += 1

    print(prime_factors)
    return prime_factors[-1]

print(largest_prime_factor(600851475143))
