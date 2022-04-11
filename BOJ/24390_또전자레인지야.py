import sys
input = sys.stdin.readline

M, S = map(int, input().split(":"))

ans = 0
ans += M // 10 # 10분 버튼
M %= 10
ans += M # 1분 버튼

if (S//30 != 0):
    ans += S // 30
else:
    ans += 1 # 시작버튼
ans += (S % 30) // 10
print(ans)
