# 20. Определить, присутствует ли в заданном списке строк, некоторое число 

# from curses.ascii import isdigit


list = ['qwe', 'qwer', '3', 'qwert', '16', 'qwerty']
# list = ['qwe', 'qwer', 'qwert', 'qwerty']
print(list)

def find_num_in_string(numbers):
    num = ''
    for elem in numbers:
        if elem.isdigit():
            num = num + elem
            return num
    
print(find_num_in_string(list))