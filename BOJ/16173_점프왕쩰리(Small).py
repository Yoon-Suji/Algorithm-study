import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
arr = []
dx = [1, 0]
dy = [0, 1]
for _ in range(N):
    arr.append(list(map(int, input().split())))

flag = False
visit = [[False]*N for _ in range(N)]
def sol(x, y):
    global flag
    if (x>=N or y>=N or visit[x][y]==True):
        return
    visit[x][y] = True
    if (arr[x][y]==-1):
        print("HaruHaru")
        sys.exit(0)
    move = arr[x][y]
    sol(x+move , y) # 오른쪽
    sol(x, y+move) # 아래

sol(0,0)
print("Hing")
