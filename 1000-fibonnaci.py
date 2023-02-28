flag = True
num1 = 1
num2 = 1
count = 0
while(flag):
    if(len(str(num2))==1000):
        print(count+2)
        flag = False
    else:
        temp = num1
        num1 = num2
        num2 = temp + num2
        count = count + 1