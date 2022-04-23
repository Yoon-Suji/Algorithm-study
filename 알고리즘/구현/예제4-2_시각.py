import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            time = str(i)+str(j)+str(k)
            if '3' in time:
                cnt += 1

print(cnt)
