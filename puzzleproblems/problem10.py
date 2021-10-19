from seive_eratosthenes import seive

def get_prime_list(n=100):
    """Generate a list of all primes < n."""
    plist = [2, 3, 5]
    fac = 7
    while fac < n:
        is_prime_list = []
        if (not (fac % 3 == 0)) & (not (fac % 5 == 0)):
            for p in plist:
                is_prime_list.append(fac % p == 0)
            if not any(is_prime_list):
                plist.append(fac)
        fac += 2
    return plist

def get_list_sum(n=100):
    # plist = get_prime_list(n)
    plist = seive(n)
    return sum(plist)

n = 2000000
# print(get_prime_list(n))
print(get_list_sum(n))
