def sum_of_squares(num_list=list(range(1, 101))):
    """Determine the sum of n**2 for all 1<=n<=100."""
    total = 0
    for n in num_list:
        total += n**2
    return total

def square_of_sums(num_list=list(range(1, 101))):
    """Determine the square of the sum of all 1<=n<=100."""
    total = sum(num_list)
    return total**2

def difference(num1, num2):
    """Get the difference between the 2 numbers input 
    (absolute value, since we only care about the distance between them.
    """
    return abs(num1 - num2)

print(difference(sum_of_squares(), square_of_sums()))