No_primes = 0


def is_prime(a):
    return a > 1 and all(a % i for i in range(2, a))


for x in range(2, 99999999):
    b = is_prime(x)
    if b is True and No_primes < 10000:
        No_primes += 1
        print(No_primes)
    elif b is True and No_primes == 10000:
        print(x)
        quit()

