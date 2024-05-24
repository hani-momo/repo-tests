a = [-3, 5, 0, -8, 1, 10]
n = len(a) 

for i in range(1, n):
    
    for j in range(i, 0, -1):
        if a[j] < a[j-1]:
            a[j], a[j - 1] = a[j - 1], a[j]
        else:
            break 

print(a) 
