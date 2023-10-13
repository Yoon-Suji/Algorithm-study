import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = []
    for i in range(0, M * N, M):
        dp.append(arr[i:i+M])
    
    for y in range(1, M):
        for x in range(N):
            if (x == 0): left_up = 0
            else: left_up = dp[x-1][y-1]
            if (x == N-1): left_down = 0
            else: left_down = dp[x+1][y-1]
            left = dp[x][y-1]
            dp[x][y] = max(left_up, left, left_down) + dp[x][y]
    
    answer = 0
    for i in range(N):
        answer = max(answer, dp[i][M-1])
    print(answer)
