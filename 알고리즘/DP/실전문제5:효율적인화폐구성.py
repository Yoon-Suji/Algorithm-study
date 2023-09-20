import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
dp = [10001] * (M + 1)
dp[0] = 0
for i in range(N):
    money = int(input())
    for j in range(money, M + 1):
        if (dp[j - money] != 10001):
            dp[j] = min(dp[j - money] + 1, dp[j])

if (dp[M] == 10001): print(-1)
else: print(dp[M])
