# 20. Определить, присутствует ли в заданном списке строк, некоторое число 

def find_number(n):
    string1 = ['jh', 'sdhfogf', 'kjahsd', '24', 'dpo', '7']
    N = str(n)
    for i in range(len(string1)):
        if N in string1:
            return True
        else:
            return False
print(find_number(24))