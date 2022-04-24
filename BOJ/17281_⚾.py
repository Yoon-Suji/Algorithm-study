import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline

N = int(input())
scores = []
for _ in range(N):
    scores.append(list(map(int, input().split())))

num = [1, 2, 3, 4, 5, 6, 7, 8]
order = permutations(num, 8)

ans = 0
for i in list(order):
    player = list(i)
    player.insert(3, 0)
    
    idx = 0 # player index
    result = 0
    j = 0 # inning
    out = 0
    b1, b2, b3 = 0, 0, 0
    
    while (j < N):
        
        if (out == 3):
            j += 1
            out = 0
            b1, b2, b3 = 0, 0, 0
            continue
        
        score = scores[j][player[idx]]

        if (score == 0):
            out += 1

        elif (score == 1):
            result += b3
            b1, b2, b3 = 1, b1, b2

        elif (score == 2):
            result += b2 + b3
            b1, b2, b3 = 0, 1, b1

        elif (score == 3):
            result += b1 + b2 + b3
            b1, b2, b3 = 0, 0, 1
        
        else:
            result += b1 + b2 + b3 + 1
            b1, b2, b3 = 0, 0, 0
            
        idx = (idx + 1) % 9
        
    ans = max(ans, result)
print(ans)
    
