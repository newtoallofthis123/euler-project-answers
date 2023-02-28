def factorial(n):
    product = 1
    while(n>0):
        product=product*n
        n=n-1
    return product

def add_digs(num):
    nums = str(num)
    sum = 0
    for i in nums:
        sum = sum + int(i)
    return sum

num = int(input("Enter The number: "))
product = factorial(num)
print(product)
print(add_digs(product))