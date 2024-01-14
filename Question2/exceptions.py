try:
    name = input("Enter the name of the user \n")

    # This line below will cause a NameError
    print(x)

    # This line below will cause arithmetic error
    value = 3 / 0

except KeyboardInterrupt:
    print("Hello user. You have pressed ctrl-c button.")
except NameError:
    print("Variable x has not been defined")
except ArithmeticError:
    print("This arithmetic operation is invalid")
# if no error, the else part will be printed
else:
    print("Hello ")
