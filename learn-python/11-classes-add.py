print('classes-add')
print('****************************************************************************************************')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

# each calls the constructor __init__
p1 = Point(1, 2)
p2 = Point(3, 4)

# uses __add__
p4 = p1 + p2
print(p4.x, p4.y)

# self = p1, other = p2, uses add
p3 = p1.add(p2)
print(p3.x, p3.y)  

