result = 0
num1 = 0
num2 = 1
next_number = num2  
count = 1

while next_number<4*10**6:
    if next_number&1 == 0:
        result += next_number

    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2

print(result)