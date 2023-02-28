def is_prime(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    return prime

count = 0

for num in range(2, 1000000):
    import itertools
    if is_prime(num):
        result = list(itertools.permutations(str(num)))
        for i in result:
            printable = True
            if not is_prime(int(''.join(i))) or ''.join(i).startswith("0"):
                printable = False
        if printable:
            count += 1

print(count)