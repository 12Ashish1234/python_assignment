class FirstClass:
    def testMethod(self):
        print("In First Class")


class SecondClass(FirstClass):
    def testMethod(self):
        print("In Second Class")


class ThirdClass(FirstClass):
    def testMethod(self):
        print("In Third Class")


# This gives output of method from Second class
# class FourthClass(SecondClass, ThirdClass):
#     pass


# This gives output of method from ThirdClass class
class FourthClass(ThirdClass, SecondClass):
    pass


obj = FourthClass()
obj.testMethod()
