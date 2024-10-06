import seaborn as sns
import matplotlib.pyplot as plt


class PrimeChecker:
    def __init__(self):
        self.seen = set()
        self.primeset = set()
        self.primeDict = dict()

    @staticmethod
    def factors(n):
        """
        Gets the factors of n
        :param n: number that you want the factors of
        :type n: int
        :return: a sorted list of factors
        :rtype: set
        """

        factor_list = set()
        for z in range(1, int(n ** 0.5) + 1):
            if n % z == 0:
                factor_list.add(z)
                factor_list.add(n // z)
        return sorted(factor_list)

    def PrimeCheck(self, i, fast=False):

        if i in self.seen:
            return print(self.primeDict[i])
        if i < 2:
            assert ValueError
        if type(i) is float:
            i = int(i)
        if type(i) is not int:
            assert TypeError
        self.seen.add(i)

        if fast:

            for p in range(1, int(i**0.5) + 1):  # use this to check faster
                factor_list = self.factors(p)
                if factor_list == [1, p]:
                    self.primeset.add(p)
                    self.primeDict[p] = 'Yes'
                else:
                    self.primeDict[p] = 'No'

            for x in self.primeset:  # Just checks prime values of the number and if they divide
                if i % x == 0:
                    self.primeDict[i] = 'No'

            #        return_text = '{} {} is not prime'.format(self.primeDict[i], i)
            #        return return_text

                    return False

            self.primeset.add(i)
            self.primeDict[i] = 'Yes'

    #        return_text = '{} {} is prime'.format(self.primeDict[i], i)

            return True

    #        return return_text  # useful for testing one prime and not all beneath, same with below
    #        return print(self.primeDict, '\n', sorted(self.primeset), '\n', return_text)

        else:
            for p in range(1, i + 1):  # use this for sns view
                factor_list = self.factors(p)
                if factor_list == [1, p]:
                    self.primeset.add(p)
                    self.primeDict[p] = 'Yes'
                else:
                    self.primeDict[p] = 'No'
            return sorted(self.primeset)



# checker = PrimeChecker().PrimeCheck
# result = checker
# print(result)
# sns.histplot(data=result, bins=1)  # Shows primes within of result and their distributions
# plt.show()
