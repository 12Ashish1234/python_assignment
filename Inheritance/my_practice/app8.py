class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x * self.y == other.x * other.y


obj1 = A(5, 2)
obj2 = A(2, 5)
print(obj1 == obj2)
