'''
2. Шахматная ладья ходит по горизонтали или вертикали. 
Даны две различные клетки шахматной доски, определите, может ли ладья попасть с первой клетки на вторую одним ходом.
Входные данные:
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
Выходные данные:
Программа должна вывести YES, если из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае
'''

# Допустим, что координатами будут считаться x и y, и только в качестве чисел: 1-8, где x - строка, y - столбец

kx1 = int(input('Координаты \'x\' первой ладьи: '))
ky1 = int(input('Координаты \'y\' первой ладьи: '))
kx2 = int(input('Координаты \'x\' второй ладьи: '))
ky2 = int(input('Координаты \'y\' второй ладьи: '))

if kx1 == kx2 or ky1 == ky2:
   print('YES')
else:
   print('NO')
