import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

ans = []
for i in range(N):
    ans.insert(num[i], i+1)

for i in range(N-1, -1, -1):
    print(ans[i], end=" ")
