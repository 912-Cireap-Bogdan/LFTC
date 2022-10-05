
# compute the sum of n numbers
def sum_of_n_numbers(list_of_numbers):
    res = 0
    for number in list_of_numbers:
        res = res + number
    
    return res

print(sum_of_n_numbers([1,2,3,4]))