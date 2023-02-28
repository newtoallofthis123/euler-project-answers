def get_num():
    string = "0."
    num = 1
    while(len(str(string)) < 1000005):
        string = string + str(num)
        num = num + 1
    return string

# print(get_num())
num_list = [2, 1001, 10001, 100001, 1000001]
product = 1
for i in num_list:
    product = product * int(get_num()[i])

print(product)