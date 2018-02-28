# Euclid's algorithm


def gcd(m, n):
    if m < n:
        m, n = n, m
    if m % n == 0:
        return n
    else:
        diff = m - n
        return gcd(n, diff)


print("GCD of 10 and 20 is",gcd(10, 20))
