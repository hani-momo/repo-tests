a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

def area(a, b, c):
	p = (a+b+c)/2
	s = (p*(p-a)*(p-b)*(p-c))**0.5
	return(s)

print(area(a, b, c))