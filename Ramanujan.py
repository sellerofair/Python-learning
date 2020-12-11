from math import pow

count = 0
n = 1729
while count < 10:
    ok = False
    rng = int(pow(n, 1 / 3))
    for a in range(1, rng + 1):
        for b in range(a, rng + 1):
            if a ** 3 + b ** 3 == n:
                if ok:
                    print(n)
                    count += 1
                    break
                else:
                    ok = True
    n += 1