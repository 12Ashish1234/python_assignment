class Point:
    def __init__(self, tx, ty) -> None:
        self.x = tx
        self.y = ty

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def setx(self, tx):
        self.x = tx

    def sety(self, ty):
        self.y = ty

    def __repr__(self) -> str:
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])


p1 = Point(1, 5)
p2 = Point(3, 10)

print("p1- ", p1)
print("p2- ", p2)
