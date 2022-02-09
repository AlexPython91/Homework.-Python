# 31. Составить список простых множителей натурального числа N

def make_a_list(n):
    i = 2
    new_list = []
    while n != 1: 
        if n % i == 0:
            new_list.append(i) 
            n = n / i
            i = 2
        else: 
            i += 1
    return (new_list)
print (make_a_list(100))
