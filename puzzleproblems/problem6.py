def sum_of_squares(num_list=list(range(1, 101))):
    total = 0
    for n in num_list:
        total += n**2
    return total

def square_of_sums(num_list=list(range(1, 101))):
    total = sum(num_list)
    return total**2

def difference(num1, num2):
    return abs(num1 - num2)

print(difference(sum_of_squares(), square_of_sums()))