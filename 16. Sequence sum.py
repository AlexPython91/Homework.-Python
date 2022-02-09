# 16. Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму

n = int(input('Enter number: '))

def get_list(n):
    result = [round((1 + 1 / i)**i, 4) for i in range(1, n + 1)]
    return result

numbers = get_list(n)
print(numbers)
print(round(sum(numbers)))
