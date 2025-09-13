# Create a generator that yields infinite prime numbers (use 'yield` and a loop)

def infinite_primes():
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

prime_gen = infinite_primes()
for _ in range(10):  # Print first 10 primes
    print(next(prime_gen), end=" ")