import numpy as np

def seive(n=2000):
    """Generate a list of all primes < n, using a seive."""
    all_num_arr = np.arange(n)
    is_prime_arr = [True] * len(all_num_arr)

    p = 2
    # since any mutliples by smaller numbers will have been eliminated already
    while p**2 < n:
        if is_prime_arr[p]:
            for i in range(p**2, n, p):
                is_prime_arr[i] = False
        p += 1

    prime_arr = []
    for idx in range(2, n):
        if is_prime_arr[idx]:
            prime_arr.append(all_num_arr[idx])

    return prime_arr

# print(seive(2000000))
