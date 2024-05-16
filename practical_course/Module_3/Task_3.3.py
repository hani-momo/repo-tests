def create_num(m):
    m.sort(reverse=True)  # массив наоборот
    result = ''.join(str(num) for num in m) # преобразование в строку
    return result

massive = input('Массив через пробел: ')
massive = massive.split()
massive = [int(num) for num in massive]
print(massive)
print(create_num(massive))

