# Numbers where n^2 - n + C = prime for n < C
# Based on Numberphile video "Caboose Numbers"

exec(open("Primality Check.py", "r").read())

# noinspection PyUnresolvedReferences
checker = PrimeChecker().PrimeCheck



def Caboosity(c):
    caboose = True
    for n in range(1, c):  # Checks all values under C
        value = n ** 2 - n + c
        test = checker(value, fast=True)
        if not checker(value, fast=True):  # Does a fast check for if the value isn't prime
            print(f"{c} isn't Caboose")
            print(test)
            caboose = False
            break
    if caboose:
        print(f'{c} is Caboose')

Caboosity(5)
Caboosity(11)
Caboosity(17)
Caboosity(41)

size = checker(10 ** 6)  # Gets all primes under a million
for C in size:  # Checks all primes under a million
    Caboosity(C)
