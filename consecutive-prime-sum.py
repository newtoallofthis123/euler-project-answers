from itertools import permutations

digits = permutations("012345")

def is_prime(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    return prime

def get_prime(digit):
    nums = []
    for num in digit:
        if ''.join(num)[0] != "0":
            if is_prime(int(''.join(num))):
                nums.append(int(''.join(num)))
    return nums

print(get_prime(digits))