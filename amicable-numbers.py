def divisors(num):
    response = []
    sum = 0
    for i in list(range(1, num)):
        if num % i == 0:
            response.append(i)
            sum = sum + i
    return sum


sum = 0
for num in list(range(0, 10000)):
    if num == divisors(divisors(num)):
        sum = sum + num
    else:
        pass
print(sum)