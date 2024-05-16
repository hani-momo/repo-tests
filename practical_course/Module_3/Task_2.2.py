from random import randint

n = 5
m = [[randint(0, 100) for i in range(n)] for j in range(n)]

max_num = m[0][0]  # изначальные координаты элемента

for line in m:
    for num in line:
        if num > max_num:
            max_num = num
print(max_num)