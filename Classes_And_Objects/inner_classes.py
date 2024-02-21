class Student:

    def __init__(self, name, rollno) -> None:
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(f"name: {self.name}, roll number: {self.rollno}")
        self.lap.show()

    # inner class
    class Laptop:

        def __init__(self) -> None:
            self.brand = "Acer"
            self.cpu = "i9"
            self.ram = 32

        def show(self):
            print(f"brand: {self.brand}, CPU: {self.cpu}, RAM: {self.ram} GB")


s1 = Student("Tony", 3)
s2 = Student("Natalie", 5)

s1.show()

# lap1 = s1.lap
# lap2 = s2.lap

# print(id(lap1))
# print(id(lap2))
