from itertools import permutations


def is_substring_divisible(number):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        substring = int(str(number)[i:i+3])
        if substring % primes[i-1] != 0:
            return False
    return True


digitals = permutations("0123456789")
sum = 0
for digital in digitals:
    if digital[0] != "0":
        number = int("".join(digital))
        if is_substring_divisible(number):
            sum += number

print(sum)
