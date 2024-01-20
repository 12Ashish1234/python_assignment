class ReverseIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = len(sequence) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            value = self.sequence[self.index]
            self.index -= 1
            return value
        else:
            raise StopIteration()


my_sequence = [1, 2, 3, 4, 5]
reverse_iterator = ReverseIterator(my_sequence)

for value in reverse_iterator:
    print(value)
