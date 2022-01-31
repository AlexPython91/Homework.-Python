# 14. Подсчитать сумму цифр в вещественном числе 

num = 2.455679

def sum_numbers(number):
    # x = str(number)
    res = 0
    for i in str(number):
        if i != '.':
            res += int(i)
    return res

print(sum_numbers(num))