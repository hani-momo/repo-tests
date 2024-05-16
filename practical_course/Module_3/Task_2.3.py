d = {'1':'0',
'3':'2',
'5':'4', 
}
print(d)

n = {}

for key, value in d.items():
    n[value] = key
   
print(n)