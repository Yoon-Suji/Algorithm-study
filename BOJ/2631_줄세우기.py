# 2631번 줄세우기
import sys
input = sys.stdin.readline

N = int(input())
kids = []
for _ in range(N):
    kids.append(int(input()))

dp = [1] * (N+1) #kids[i]를 마지막 원소로 가질 때 가장 긴 증가하는 부분 수열의 길이
for i in range(N):
    for j in range(i):
        if (kids[i] > kids[j]):
            dp[i] = max(dp[i], dp[j]+1)
print(N - max(dp))
