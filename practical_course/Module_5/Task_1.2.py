   class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_zero(self):
        return (self.x ** 2 + self.y ** 2) ** (1/2)

    def distance_points(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5


x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

point1 = Point(x1, y1)
point2 = Point(x2, y2)


distance_zero = point1.distance_zero()
print('distance from the first point to 0, 0 = ', distance_zero)
distance_zero = point2.distance_zero()
print('distance from the second point to 0, 0 = ', distance_zero)

distance_points = point1.distance_points(point2)
print("distance between two points is ", distance_points)
