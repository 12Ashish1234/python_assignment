class Student:
    school = "telusko"

    def __init__(self, m1, m2, m3) -> None:
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # class method
    @classmethod
    def getSchool(cls):
        print(f"name of school: {cls.school}")

    # static method
    @staticmethod
    def info():
        print("some info about school")


s1 = Student(34, 55, 22)
s2 = Student(67, 68, 100)

print(s2.avg())

s1.getSchool()
s1.info()