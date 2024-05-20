def sort_mas(mas):
    mas = mas.split(',')

    mas = [int(x) for x in mas]

    m = sorted([str(x) for x in mas], reverse=True)

    number = ''.join(m)

    return number

mas = input('Your numbers with comma: ')

result = sort_mas(mas)
print(result)
