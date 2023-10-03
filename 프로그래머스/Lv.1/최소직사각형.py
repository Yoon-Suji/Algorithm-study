def solution(sizes):
    sorted_w = sorted(sizes, key=lambda x: x[0])
    sorted_h = sorted(sizes, key=lambda x: x[1])
    a = max(sorted_w[-1][0], sorted_h[-1][1])
    b = 0
    for i in range(len(sizes)):
        b = max(min(sizes[i]), b)
    answer = a * b
    return answer
