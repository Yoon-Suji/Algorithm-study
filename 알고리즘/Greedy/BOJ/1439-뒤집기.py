import sys
input = sys.stdin.readline

S = input().rstrip() + '2'
cnt = [0, 0]
for i in range(len(S)-1):
    if (S[i] != S[i+1]):
        cnt[int(S[i])] += 1
print(min(cnt))
