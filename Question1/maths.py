from calc import factorial, logFunction, degreeToRadians, calc_trig

# finding factorial
num1 = input("Enter a number to find factorial: ")
num1 = int(num1)
factorial = factorial(num1)
if factorial == -1:
    print("Sorry, factorial does not exist for negative numbers")
else:
    print("Factorial is: ", factorial)

print()


# finding log10 of a number
num2 = input("Enter a number to find the log10 of a number: ")
num2 = int(num2)
print("Log10 of {} is : ".format(num2), logFunction(num2))
print()


# converting value in degrees to radians
num_degree = input("Enter a degree value: ")
num_degree = int(num_degree)
print("Value in Radians: ", degreeToRadians(num_degree))
print()


# to find sine, cosine and tangent values of a given angle
num_angle = input("Enter an angle: ")
num_angle = int(num_angle)
values = calc_trig(num_angle)
print("Sine of {} is: ".format(num_angle), values[0])
print("Cosine of {} is: ".format(num_angle), values[1])
print("Tangent of {} is: ".format(num_angle), values[2])
print()
