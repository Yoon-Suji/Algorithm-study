import sys
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    array.append(list(input().split()))

array.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
print(array)
for i in array:
    print(i[0])
    
