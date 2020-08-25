def countdown(start: int, stop: int):
    """
    Simple recursion, for example:
    if arguments (4, -2) result will be 4 3 2 1 0 -1 -2

    :param start: int
    :param stop: int
    :return:
    """
    print(start)

    if start > stop:
        countdown(start - 1, stop)
    else:
        print('-' * 10)  # Just for visualize


def countup(start: int, stop: int):
    """
    Simple recursion, for examle:
    if arguments (1, 5) result will be 1 2 3 4 5
    :param start: int
    :param stop: int
    :return:
    """
    print(start)

    if stop > start:
        countup(start + 1, stop)
    else:
        print('-' * 10)  # Just for visualize


countdown(4, -2)
countup(4, 10)
