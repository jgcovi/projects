def nth_prime(n=6):
    """Return the nth prime."""
    plist = [2, 3]
    fac = 5
    while len(plist) < n:
        is_prime_list = []
        if not (fac % 3 == 0):
            for p in plist:
                is_prime_list.append(fac % p == 0)
            if not any(is_prime_list):
                plist.append(fac)
        fac += 2
    return plist[-1]

print(nth_prime(10001))