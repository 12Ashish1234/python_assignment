class A:
    def __init__(self):
        print("Init in A")


class B(A):
    def __init__(self):
        A.__init__(self)


def main():
    b = B()


main()
