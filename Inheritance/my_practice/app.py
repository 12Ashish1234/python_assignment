# if a class's __new__ method returns an instance, the __init__ method will be automatically called.

class Demo:
    def __new__(self):
        print("Demo's __new__() invoked")
        # The default __new__ implementation returns a new instance of the class
        instance = super(Demo, self).__new__(self)
        return instance

    def __init__(self):
        print("Demo's __init__() invoked")


class Derived_Demo(Demo):
    def __new__(self):
        print("Derived_Demo's __new__() invoked")
        instance = super(Derived_Demo, self).__new__(self)
        return instance

    def __init__(self):
        print("Derived_Demo's __init__() invoked")


def main():
    obj1 = Derived_Demo()
    obj2 = Demo()


main()
