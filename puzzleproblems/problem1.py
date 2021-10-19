def is_multiple_of_3(n):
    return (n % 3) == 0

def is_multiple_of_5(n):
    return (n % 5) == 0

def get_all_multiples(n):
    """Generate all multiple of 3 and 5 which are less than n."""
    i = 0
    multiple_list = []
    for i in range(n):
        if is_multiple_of_3(i) | is_multiple_of_5(i):
            multiple_list.append(i)
    return multiple_list

print(sum(get_all_multiples(1000)))