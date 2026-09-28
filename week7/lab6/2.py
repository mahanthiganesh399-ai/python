def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

numbers = list(range(1, 51))

primes = list(filter(is_prime, numbers))

print("Prime numbers:", primes)