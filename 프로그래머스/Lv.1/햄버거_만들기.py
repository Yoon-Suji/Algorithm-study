def solution(ingredient):
    arr = ''
    answer = 0
    for i in range(len(ingredient)):
        arr += str(ingredient[i])
        if (len(arr) >= 4 and arr[-4:] == '1231'):
            answer += 1
            arr = arr[:-4]
    return answer
