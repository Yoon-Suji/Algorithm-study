def solution(s, n):
    # print(ord('A'), ord('Z'), ord('a'), ord('z'))
    answer = ''
    for i in s:
        if (i == ' '): 
            answer += i
            continue
        # 소문자일때
        if (ord(i) >= 97 and ord(i) + n > 122):
            answer += chr((ord(i) + n) - 26)
            continue
        # 대문자일때    
        if (ord(i) <= 90 and ord(i) + n > 90):
            answer += chr((ord(i) + n) - 26)
            continue
        else:
            answer += chr((ord(i) + n))
        
    return answer
