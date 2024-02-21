class Test:
    z = 10
    def __init__(self):
        self.x = 0

    def display(self):
        print("display function of base class")


class Derived_Test(Test):
    def __init__(self):
        super().__init__()
        self.y = 1


def main():
    b = Derived_Test()
    # print(b.x, b.y)
    print(b.z)
    b.display()


main()
