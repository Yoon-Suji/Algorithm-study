import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cnt = 0

while (N > 1):
    if (N%K == 0):# N이 K로 나누어떨어지면 나누기
        cnt += 1
        N //= K
    else:
        cnt += N % K # 나누어떨어지지 않으면 나누어떨어질때까지 1씩 빼기
        N = N - (N%K)
    
print(cnt-1) # 0이 될때까지 빼게 되므로 cnt 하나 빼서 출력
