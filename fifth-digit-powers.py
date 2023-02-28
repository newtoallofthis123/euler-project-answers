sum = 0

for num in range(2, 1000000):
    range_sum = 0
    for i in str(num):
        range_sum = range_sum + pow(int(i), 5)
    if num == range_sum:
        sum = sum + num 

print(sum)