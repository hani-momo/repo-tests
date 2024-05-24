def compare(a, b):
    return str(a) + str(b) > str(b) + str(a)

def max_num(numbers):
    for i in range(len(numbers)):
        item = numbers[i]  
        j = i  

        while j > 0 and compare(item, numbers[j - 1]):
            numbers[j] = numbers[j - 1] 
            j -= 1  

        numbers[j] = item  

    result = ''.join(str(x) for x in numbers)  
    print(result)  

array = [21, 22, 2, 29]  
max_num(array)  
