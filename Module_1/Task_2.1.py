'''
1. Даны три целых числа. Определите, сколько среди них совпадающих. 
Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).
'''

x = int(input('1st number: '))
y = int(input('2nd number: '))
z = int(input('3rd number: '))

if x == y == z:
   print(3)
elif x == y or y == z or x == z:
   print(2)
else:
   print(0)


