def is_prime(n):
    """Determine if a number is prime. (My initial - naive - implementation)."""
    # start with the most simple cases, checking against the first 2 prime numbers
    if n in [2, 3]:
        return True
    # eliminate anything divisible by the first two prime numbers
    elif ((n % 2) == 0) | ((n % 3) == 0):
        return False
    else:
        fac = 5
        is_prime = True
        while is_prime & (fac < n):
            # a modular remainder of 0 means division is successful and n is not prime
            is_prime = n % fac != 0 
            # no need to iterate through even numbers, since none > 2 are prime
            fac += 2
    return is_prime

def get_primes(n):
    """Get all prime numbers which appear in the prime factorization of n."""
    prime_list = []
    total = n
    if is_prime(n):
        return [1, n]
    else:
        if n % 2 == 0:
            prime_list.append(2)
            total /= 2
        if n % 3 == 0:
            prime_list.append(3)
            total /= 3
        fac = 5
        while fac <= total:
            if fac == total:
                prime_list.append(fac)
                return prime_list
            elif is_prime(fac) & ((total % fac) == 0):
                prime_list.append(fac)
                total /= fac
            fac += 2
    return prime_list
    

num = 600851475143
# res = is_prime(num)
# print('Is {} prime?: {}'.format(num, res))
# print()
print(get_primes(num)[-1])