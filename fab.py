def fab(n):
    """
    斐波那契数列
    时间复杂度 O(n)
    空间复杂度 O(1)
    :param n:
    :return:
    """

    if n < 0:
        return -1
    elif n < 2:
        return n

    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b
