import seaborn as sns
import matplotlib.pyplot as plt


class PrimeChecker:
    def __init__(self):
        self.primeDict = dict()


    @staticmethod
    def Sieve_of_Eratosthenes(n, fast=False):
        if fast:
            nums = set(range(2, int(n**0.5)+1))
        else:
            nums = set(range(2, n+1))
        iterators = list(nums)
        for i in nums.copy():
            for x in iterators[i**2:]:
                if x % i == 0:
                    nums.discard(x)
        return nums

    def PrimeCheck(self, i, fast=False):

        if i < 2:
            assert ValueError
        if type(i) is float:
            i = int(i)
        if type(i) is not int:
            assert TypeError

        if fast:
            primeset = self.Sieve_of_Eratosthenes(i, fast=True)

            for x in primeset:  # Just checks prime values of the number and if they divide
                if i % x == 0:
                    self.primeDict[i] = 'No'

            #        return_text = '{} {} is not prime'.format(self.primeDict[i], i)
            #        return return_text

                    return False

            primeset.add(i)
            self.primeDict[i] = 'Yes'

    #        return_text = '{} {} is prime'.format(self.primeDict[i], i)

            return True
 
    #        return return_text  # useful for testing one prime and not all beneath, same with below
    #        return print(self.primeDict, '\n', sorted(self.primeset), '\n', return_text)

        else:
            primeset = self.Sieve_of_Eratosthenes(i, fast=False)
            return sorted(primeset)



checker = PrimeChecker().PrimeCheck
result = checker(100000007, fast=True)
print(result)
# sns.histplot(data=result, bins=1)  # Shows primes within of result and their distributions
# plt.show()
