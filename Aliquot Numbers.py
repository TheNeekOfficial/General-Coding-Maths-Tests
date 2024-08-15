unknown = [276, 306, 396, 552, 564, 660, 696, 780, 828, 888, 966, 996, 1074, 1086, 1098, 1104, 1134, 1218, 1302, 1314,
           1320, 1338, 1350, 1356, 1392, 1398, 1410, 1464, 1476, 1488, 1512, 1560, 1572, 1578, 1590, 1632, 1650, 1662,
           1674, 1722, 1734, 1758, 1770, 1806, 1836]  # Values where we don't know their max no. of iterations

avoid = [702, 840, 978, 990, 1062, 1248]  # We know it ends just too big for me to test program

value_to_iter_no = dict(set())  # Used during testing to see complete list of numbers tested and their no. of iterations


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


def aliquotity(n, reiterated=False):
    """

    Goes through the Aliquot Sequence of a number and states the number of iterations it takes to get to 1 following
    the sequence

    It will check if the number is in the unknown list, where we don't know if they converge to 1 at the end of their
    aliquot sequence and then skip if it is

    It will also check if the number is in the 'avoid' list which is a list I've made just going through the numbers
    and seeing the program get stuck for a long time at a value. They have been solved, but it typically goes to ~20
    digits long. That's about the point I determined this was too long, and I wasn't willing to wait for it.
    Feel free to change this list at will

    :param n: Number that you want to see the aliquot sequence of
    :type n: int
    :param reiterated: Value used in recursive aspect of this to not reset values that need to stay between recursions
    : between type reiterated: bool
    :return: Number of iterations, the value you entered and if it looped, the loop it got stuck at
    :rtype: str
    :raises: TypeError: if n isn't int
    """

    global no_of_iters
    global original
    global seen

    if not reiterated:
        no_of_iters = 0
        original = n
        seen = set()

    return_message = f"{no_of_iters} is the number of iterations this took to reach the end of {original}'s aliquotity"
    # added to reduce repitions of that exact messaging in return prints

    if type(n) is not int:
        print('TypeError: input needs to be int')
        raise TypeError

    if n == 1:
        value_to_iter_no[original] = no_of_iters
        return print(return_message)

    if original in unknown:
        return aliquotity(original + 1)

    if original in avoid:
        return aliquotity(original+1)

    if n in seen:
        value_to_iter_no[original] = no_of_iters
        return print(f'{return_message} and reached a loop at n = {n}')

    seen.add(n)
    factor_list = factors(n)
    total = sum(y for y in factor_list if y != n)

    if n == total:
        value_to_iter_no[original] = no_of_iters
        return print(f"{return_message} and reached a loop at n = {total}")

    no_of_iters += 1

    return aliquotity(total, reiterated=True)


# test values
# aliquotity(24)
# aliquotity(138)
# aliquotity(702)

search_size = 1000000
for i in range(2, search_size):
    aliquotity(i)
