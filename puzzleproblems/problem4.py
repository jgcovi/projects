def is_palindrome(n):
    """Determine if a number or string is a palindrome."""
    num_str = str(n).lower()
    flip_str = num_str[::-1]
    is_pal = False
    if len(num_str) % 2 == 0:
        is_pal = num_str == flip_str
    else:
        middle = int(len(num_str) / 2)
        is_pal = num_str[:middle] == flip_str[:middle]
    return is_pal

def generate_palindrome(dig_size=3):
    """Generate a list of palindromes and return the largest.
    TODO: optimize this code so doesn't have to run through all pairings."""
    start = int('9' * dig_size)
    end = int('9' * (dig_size - 1))
    
    pal_list = []
    for p1 in range(start, end, -1):
        for p2 in range(start, end, -1):
            prod = p1 * p2
            if is_palindrome(prod):
                pal_list.append(prod)
            p2 -= 1
        p1 -= 1
        
    return max(pal_list)

print(generate_palindrome(3))
# print(is_palindrome('Ada'))