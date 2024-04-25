def find_peak(list_of_integers):
    """
    Trying to Find the peak in a list of unsorted integers.

    Args:
        list_of_integers : A list of unsorted integers.

    Returns:
        int: A peak integer that we find in the list.
    """
    if not list_of_integers:
        return None

    descend = 0
    top = len(list_of_integers) - 1

    while descend < top:
        middle = (descend + top) // 2

        if list_of_integers[middle] < list_of_integers[middle + 1]:
            descend = middle + 1
        else:
            top = middle

    return list_of_integers[descend]
