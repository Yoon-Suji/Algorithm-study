import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    tmp = []
    for _ in range(5):
        tmp.append(list(input().rstrip()))
    arr.append(tmp)

minCnt = 36
a, b = -1, -1
for i in range(N-1):
    for j in range(i+1, N):
        cnt = 0
        for k in range(5):
            for s in range(7):
                if (arr[i][k][s] != arr[j][k][s]):
                    cnt += 1
        if (cnt < minCnt):
            minCnt = cnt
            a = i+1
            b = j+1
print(a,b)

