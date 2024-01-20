class LengthComparison:
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        if not isinstance(other, LengthComparison):
            raise ValueError("Comparison with unsupported type")
        
        return len(self.value) > len(other.value)


str1 = LengthComparison("Hello")
str2 = LengthComparison("World")

if str1 > str2:
    print(f"{str1.value} is longer than {str2.value}")
elif str1 < str2:
    print(f"{str1.value} is shorter than {str2.value}")
else:
    print(f"{str1.value} and {str2.value} have the same length")
