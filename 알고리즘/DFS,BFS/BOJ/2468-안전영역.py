import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, visited, arr, W):
    st = [(x, y)]
    while st:
        cur = st.pop()
        for i in range(4):
            xx = cur[0] + dx[i]
            yy = cur[1] + dy[i]
            if (0<=xx<N and 0<=yy<N and visited[xx][yy] == False and arr[xx][yy] > W):
                st.append((xx, yy))
                visited[xx][yy] = True


ans = 1
for w in range(101):
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if (arr[i][j] > w and visited[i][j] == False):
                cnt += 1
                dfs(i, j, visited, arr, w)
    ans = max(ans, cnt)
    
print(ans)
