#  def fibonacci(n):
#     """Recursively get nth term of the Fibonacci sequence."""
#     if n == 2:
#         return 2
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_seq(n):
    """Generate the Fibonnaci sequence of terms < n.
    (Starting at 1 with pattern [1, 2, ...]"""
    # Establish the base cases
    seq = [1, 2]
    idx = len(seq)

    while (seq[-1] + seq[-2]) < n:
        if n == 1:
            return seq[0]
        elif n == 2:
            return seq[1]
        else:
            seq.append(seq[idx-1] + seq[idx-2])
        idx += 1
    return seq

def even_fib(n):
    """Calculate the sum of all even terms of the Fibonacci sequence up to n."""
    seq = fibonacci_seq(n)
    total = 0
    for term in seq:
        if term % 2 == 0:
            total += term
    return total

print(even_fib(4000000))
