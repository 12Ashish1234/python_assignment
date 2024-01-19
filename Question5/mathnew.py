import math


class MathOperations:
    def sqroot(self, num):
        return math.sqrt(num)

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        try:
            ans = num1 / num2
            return ans
        except ZeroDivisionError:
            return "Cannot Divide by Zero"


class MathNew(MathOperations):
    def __init__(self):
        super().__init__()


# object of MathNew
obj = MathNew()

print("Square Root:", obj.sqroot(16))
print("Addition:", obj.addition(7, 3))
print("Subtraction:", obj.subtraction(8, 2))
print("Multiplication:", obj.multiplication(5, 6))

# Division with try-except block
try:
    result = obj.division(15, 1)
    print("Division:", result)
except Exception as e:
    print("Error:", e)
