import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(input().rstrip()))

l = min(N, M)
ans = 0

for k in range(1, l):
    flag = True
    for i in range(N-k):
        for j in range(M-k):
            if (arr[i][j] == arr[i+k][j] and arr[i+k][j] == arr[i][j+k] and arr[i][j+k] == arr[i+k][j+k]):
                ans = k
                flag = False
                break
        if (flag == False): break
            
print((ans+1)**2)
