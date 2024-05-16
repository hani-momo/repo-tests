l = [1, 4, 1, 6, "hello", "a", 5, "hello"]
repeated = []
scan = []

for i in (l):
    if i not in scan:
        scan.append(i)
    else:
        repeated.append(i)

print('Повторяющие элементы списка:', repeated)