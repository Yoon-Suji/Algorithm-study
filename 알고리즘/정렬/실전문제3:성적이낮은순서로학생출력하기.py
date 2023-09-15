import sys
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    array.append(input().split())
array.sort(key = lambda x : int(x[1]))
for name, _ in array:
    print(name, end = '')
