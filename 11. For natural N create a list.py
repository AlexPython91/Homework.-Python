# 11. Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.

n = int(input('Enter number: '))

def get_natural_set(n):
    new_set = {1}
    for elem in range(n):
        if elem % 2 != 0:
            new_set.add(-3**elem)
        else:
            new_set.add(3**elem)
    return new_set
print(get_natural_set(n))