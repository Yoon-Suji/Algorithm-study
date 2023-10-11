# BOJ 1439
import sys
input = sys.stdin.readline

s = input()
arr = [0, 0]
for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        arr[int(s[i])] += 1

print(min(arr))
