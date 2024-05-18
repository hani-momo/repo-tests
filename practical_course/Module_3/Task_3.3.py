def create_num(m):
    result = ''.join(str(num) for num in m) # преобразование в строку
    result = list(result)
    '''m.sort(reverse=True)  # массив наоборот'''
    result = sorted(result, reverse = True)
    result = ''.join(result)
    return result

massive = input('Массив через пробел: ')
massive = massive.split()
massive = [int(num) for num in massive]
print(massive)
print(create_num(massive))
