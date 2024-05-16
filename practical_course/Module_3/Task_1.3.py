num = input('Целое число: ')
num_l = list(num) 

sum_num = 0

for i in num_l:
    sum_num += int(i)

print('Сумма цифр числа: ', sum_num)
