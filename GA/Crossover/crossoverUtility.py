def divide(lst: list, n: int) -> list:
    """
    Divides an individual's list in n parts.
    :param lst: The individual's list of exercises to divide.
    :param n: The number of parts.
    :return: A list with the divided parts.
    """
    return [lst[i * len(lst) // n: (i + 1) * len(lst) // n] for i in range(n)]
