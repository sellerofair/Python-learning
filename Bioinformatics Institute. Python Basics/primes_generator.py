def primes():
    yield 2
    yield 3
    number = 3
    while True:
        number += 2
        prime = True
        for i in range(3, int(number ** 0.5) + 1):
            if number % i == 0:
                prime = False
                break
        if prime:
            yield number