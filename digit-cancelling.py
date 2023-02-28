# Pending

def cancel(num, den):
    for i in str(num):
        if i in str(den):
            if i != '0':
                num = int(str(num).replace(i, "", 1))
                den = int(str(den).replace(i, "", 1))
                print([num, den])
                return [num, den]

def actual_division(num, den):
    result = num / den
    return result

def is_result(num1, num2):
    if actual_division(num1, num2) == actual_division(cancel(num1, num2)[0], cancel(num1, num2)[1]):
        return True

def main():
    for i in range(11, 100):
        for j in range(11, i+1):
            if is_result(j, i):
                if j / i < 1:
                    return f'{j}/{i}'

print(main())