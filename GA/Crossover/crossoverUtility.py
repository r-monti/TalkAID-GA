def divide(lst, n):
    """
    Divides an individual in n parts
    :param lst: the individual to divide
    :param n: the number of parts
    :return: a list with the divided parts
    """
    return [lst[i * len(lst) // n: (i + 1) * len(lst) // n] for i in range(n)]
