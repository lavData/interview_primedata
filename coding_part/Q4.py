import random

# Create an array random without duplicates have 0 -> n with n elements
def create_random(n):
    return random.sample(range(n + 1), n)

''' My algorithm:
    1. Compute sumary of list numbers from 0 -> n by euqation (n * (n + 1)) / 2. O(1)
    2. Compute sumary of arr. O(n)
    3. The missing number is the subtraction between the upper sum and the lower sum. O(1)
    => The complexity is O(n)
'''
def Q1(n, arr):
    upper_sum = n * (n + 1) // 2
    lower_sum = sum(arr)
    return upper_sum - lower_sum


if __name__ == '__main__':
    n = int(input("Type n: "))
    arr = create_random(n)
    print(arr, 'The missing value is', Q1(n, arr))