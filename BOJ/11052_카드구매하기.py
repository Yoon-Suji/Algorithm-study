# 11052 카드 구매하기
import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
P.insert(0, 0) # index 맞추려고

dp = [0]*(N+1)
dp[1] = P[1]
dp[2] = max(P[2], dp[1]*2)

for i in range(3, N+1):
    tmp = P[i]
    for j in range((i+1)//2, i):
        tmp = max(tmp, dp[j]+dp[i-j])
    dp[i] = tmp
print(dp[N])
