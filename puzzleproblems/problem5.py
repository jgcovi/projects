"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

def get_primes(n):
    """Get all prime factors of a number."""
    pdic={}
    # Go ahead and eliminate all 2s and 3s
    while (n % 2 == 0):
        if 2 not in pdic.keys():
            pdic[2] = 0
        pdic[2] += 1
        n /= 2

    while (n % 3 == 0):
        if 3 not in pdic.keys():
            pdic[3] = 0
        pdic[3] += 1
        n /= 3

    # starting from 5, the next prime after 3, check all odd numbers
    # since we're iterating through anything smaller, no non-prime numbers will make it into the dic
    # because we've already divided them out of N entirely, so we will be left with only primes
    i = 5
    while n != 1:
        while (n % i == 0):
            if i not in pdic.keys():
                pdic[i] = 0
            pdic[i] += 1
            n /= i
        i += 2
    return pdic

def get_least_common_divisor(min=1, max=20):
    """Get the least common divisor of all members of a list [min, ..., max]."""
    num_list = list(range(min, max+1))
    plist = []
    # get the prime factorization of all numbers in the list
    for num in num_list:
        plist.append(get_primes(num))
    
    all_pdic = {}
    for num, pdic in zip(num_list, plist):
        for k, v in pdic.items():
            if (k not in all_pdic):
                all_pdic[k] = v
            elif (v > all_pdic[k]):
                all_pdic[k] = v

    lcd = 1
    for k, v in all_pdic.items():
        lcd *= k**v
    return lcd

            

print(get_least_common_divisor())
