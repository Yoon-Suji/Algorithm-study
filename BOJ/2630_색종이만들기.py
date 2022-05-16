import sys
input = sys.stdin.realdine

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

white = 0
blue = 0
def solution(x, y, N):
    global white, blue
    color = arr[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if (color != arr[i][j]):
                solution(x, y, N//2)
                solution(x+N, y, N//2)
                solution(x, y+N, N//2)
                solution(x+N, y+N, N//2)
            if (color == 1): white+=1
            else: blue+=1
print(white)
print(blue)
