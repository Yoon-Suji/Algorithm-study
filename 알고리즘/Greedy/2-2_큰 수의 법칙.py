import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
count = M // (K+1) * K + M % (K+1) # 가장 큰 수가 더해지는 횟수
ans = count * arr[-1] + (M - count)*arr[-2]
print(ans)
