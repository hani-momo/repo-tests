x = float(input('Вклад в банке составляет: ')) # вклад
p = float(input('Ежегодное увеличение в % : ')) # % ежегод
percent = p/100 # процент в дроби для умножения
y = int(input('Необходимый минимальный предел суммы вклада: ')) # мин предел вклада через ... лет

n = 0 # года, искомая
while x < y:
    x += x*percent
    n += 1

print('Вклад составит не менее', y, 'через', n, 'лет.')