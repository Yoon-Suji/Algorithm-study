import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input().rstrip()))

n = len(arr[0])
ans = ''
for i in range(n):
    flag = False
    for j in range(N-1):
        if (arr[j][i]!=arr[j+1][i]):
            ans += '?'
            flag = True
            break
    if (flag != True):
        ans += arr[0][i]
print(ans)
