def gcd(m, n):
    for i in range(min(m,n) + 1, 1, -1):
        if m % i == 0  and n % i == 0 :
            return i
    else:
        return 1

print("GCD of 10 and 20 is",gcd(10,20))
