class A:
    def __init__(self) -> None:
        print("Init of A")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B:

    def __init__(self) -> None:
        # super().__init__()
        print("Init of B")

    def feature1(self):
        print("Feature 1 of B working")

    def feature4(self):
        print("Feature 4 working")


class C(B, A):

    def __init__(self) -> None:
        super().__init__()
        print("Init of C")


obj = C()
