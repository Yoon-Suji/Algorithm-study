import sys
input = sys.stdin.readline

T = int(input())
buttons = [300, 60, 10]
ans = []

for btn in buttons:
    ans.append(T//btn)
    T %= btn
if (T != 0):
    print(-1)
else:
    print(*ans)
