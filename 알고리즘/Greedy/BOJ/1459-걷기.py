import sys
input = sys.stdin.readline

X, Y, W, S = map(int, input().split())

s = min(X, Y) # 대각선 최대 수
w = abs(X - Y) # 직선 최소 수

if (S > 2*W):
    print(W * (w + s*2))
elif (S == 2*W or S >= W):
    print(S*s + W*w)
elif (S < W):
    print(S*(s+(w - (w%2))) + W*(w%2))
