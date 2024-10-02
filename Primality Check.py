class PrimeChecker:
    def __init__(self):
        self.seen = set()
        self.primeset = {2, 3}
        self.primeDict = dict()
    def PrimeCheck(self, i):
        if i in self.seen:
            return print(self.primeDict[i])
        if i <= 3:
            assert ValueError
        if type(i) is float:
            i = int(i)
#        if type(i) is not int:
#            assert TypeError
        self.seen.add(i)
        for n in range(2, int(i ** 0.5) + 1):
#            for x in self.primeset.copy():
#                if x % n != 0: # Doesnt work need fix
#                    self.primeset.add(n)
#                    self.primeDict[n] = 'Yes'
#                else:
#                    self.primeDict[n] = 'No'
#            if i % n != 0: also doesnt work ffs
#                self.primeset.add(i)
#                self.primeDict[i] = 'Yes'
#            else:
#                self.primeDict[i] = 'No'
#        return print(self.primeset, "{}, {} is prime".format(self.primeDict[i], i))

PrimeChecker().PrimeCheck(548)
