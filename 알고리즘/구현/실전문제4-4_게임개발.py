import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A, B, d = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

visit = [[False] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visit[A][B] = True # 시작점
cnt = 1

while (True):
    flag = False
    for i in range(4):
        d = (d-i) % 4 # 왼쪽으로 회전
        a = A + dx[d]
        b = B + dy[d]
        if (0<=a<N and 0<=b<M):
            if (maps[a][b] == 0 and visit[a][b] == False):
                cnt += 1
                visit[a][b] = True
                A = a
                B = b
                flag = True
                break
    if (flag == False):
        a = A - dx[d]
        b = B - dy[d]
        if (0<=a<N and 0<=b<M):
            if (maps[a][b] == 0):
                A = a
                B = b
            else:
                break
print(cnt)
    
