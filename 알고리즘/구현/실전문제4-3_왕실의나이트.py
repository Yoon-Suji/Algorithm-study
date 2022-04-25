import sys
input = sys.stdin.readline

n = list(input().rstrip())
n[0] = ord(n[0]) - ord('a') + 1
n[1] = int(n[1])

ans = 0
dx = [2, -2]
dy = [1, -1]

for x in dx:
    for y in dy:
        if (0 < (n[0]+x) < 9 and 0 < (n[1]+y) < 9):
            ans += 1
        if (0 < (n[0]+y) < 9 and 0 < (n[1]+x) < 9):
            ans += 1
print(ans)
