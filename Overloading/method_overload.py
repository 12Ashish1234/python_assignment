class new_class:

    def sum(self, a=None, b=None, c=None):
        sum=0
        if a!=None and b!=None and c!=None:
            sum = a + b + c
        elif a!=None and b!=None:
            sum = a+b
        else:
            sum = a
        return sum


obj = new_class()

print(obj.sum(14, 1))
