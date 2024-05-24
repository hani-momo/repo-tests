# Создаем пустой массив для хранения введенных чисел
'''a = [] # или уже заданный массив
count = 0  
while count < 10:  
    num = int(input("Enter numbers for the array (press Enter after each number): "))  
    a.append(num)  
    count += 1 '''

a = [#вписать массив]
a.sort()  
print(a) 

value = int(input('Search for: '))  

low_point = 0  
high_point = len(a) - 1  
mid = (low_point + high_point) // 2  

while value != a[mid] and low_point < high_point: 

    if value > a[mid]:  
        low_point = mid + 1 
    elif value < a[mid]: 
        high_point = mid - 1 

    mid = (low_point + high_point) // 2 

if value == a[mid]:  
    print('Index of the searched number in the array:', mid) 
else:  
    print('The searched number is not in the array')
