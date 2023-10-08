def solution(n):
    num = n ** (0.5)
    if (num.is_integer()):
        return (int(num) + 1) ** 2
    return -1
