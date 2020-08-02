def binary_search(sorted_list: list, value: str or int) -> int or False:
    low_point = 0
    high_point = len(sorted_list) - 1

    while low_point <= high_point:
        middle = (low_point + high_point) // 2
        potential_value = sorted_list[middle]

        if potential_value == value:
            return middle
        elif potential_value > value:
            high_point = middle - 1
        else:
            low_point = middle + 1
    return False


print(binary_search(['Абрикос', 'Ананас', 'Банан', 'Яблоко'], 'Банан'))
