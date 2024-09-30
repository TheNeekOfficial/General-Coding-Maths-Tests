collatz_length = []


class CollatzConjecture:
    def __init__(self):
        self.seen = set()

    def collatz_path(self, i):
        self.seen.add(i)
        if i == 1:
            global collatz_length
            collatz_length.append(len(self.seen))
            return print(len(self.seen))

        if i % 2 == 0:
            i = i / 2
        elif i % 2 == 1:
            i = ((3 * i) + 1) / 2

        return self.collatz_path(i)


for n in range(1, 10000000):
    CollatzConjecture().collatz_path(n)
print(max(collatz_length))
