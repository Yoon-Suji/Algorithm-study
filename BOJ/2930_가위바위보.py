import sys
input = sys.stdin.readline

R = int(input())
me = list(input().rstrip())
N = int(input())
friends = []
for _ in range(N):
    friends.append(list(input().rstrip()))

score = 0
max_score = 0

for j in range(R):
    m = me[j]
    S, P, R = 0, 0, 0
    tmp = {'S':0, 'P':0, 'R':0}
    for i in range(N):
        n = friends[i][j]
        tmp[n] += 1
        if (n=='S') :
            if (m == 'R'): score += 2
            elif (m == 'S') : score += 1
        elif (n=='P') :
            if (m == 'S'): score += 2
            elif (m == 'P') : score += 1
        else:
            if (m=='P'): score += 2
            elif (m=='R'): score += 1

    max_score += max(tmp['S']*2 + tmp['R'], tmp['R']*2 + tmp['P'], tmp['P']*2 + tmp['S'])
    
print(score)
print(max_score)
