'''
3. На вход подаются 2 числа. Числа могут быть как целые, так и вещественные. Сравните их значения и найдите наибольшее. 
Помните, что результатом сравнения является True или False (тип bool). При этом True эквивалентно 1, а False 0 при умножении. 
'''

a = float(input('Enter your first num: '))
b = float(input('Enter your second num: '))
c = (a > b) # вернет True или False

result = (a * c) + (b * (not c)) # наибольшее число, тк True == 1 или False == 0;
# not c == not True / not False
print(result, 'is the biggest number')
