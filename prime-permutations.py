# Pending

from itertools import permutations

digits = permutations("0123456789", 4)

def is_prime(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    return prime

def are_permutation(nums):
    actual = sorted(str(nums[1]))
    is_permutation = True
    for num in nums:
        if not sorted(num) == actual:
            is_permutation = False
    return is_permutation
        
def get_prime(digit):
    nums = []
    for num in digit:
        if ''.join(num)[0] != "0":
            if is_prime(int(''.join(num))):
                nums.append(int(''.join(num)))
    return nums

def check_diff(nums):
    # print(nums)
    if [1487, 4817, 8147] == nums:
        print("FOUND!->", nums)
    nums = sorted(nums)
    if 2*nums[1] == nums[0] + nums[2]:
        return True
    else:
        return False

nums = get_prime(digits)    

most_likely = []

for num in nums:
    result = get_prime(permutations(str(num), 4))
    if not len(result) < 3:
        most_likely.append(result)


for nums in most_likely:
    i = 0
    while i<len(nums)-2:
        if check_diff(nums[i:i+3]):
            print(True)
        i += 1