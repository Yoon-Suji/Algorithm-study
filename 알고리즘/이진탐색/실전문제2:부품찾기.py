import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
request = list(map(int, input().split()))
arr.sort()

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if (arr[mid] == target):
            return True
        elif (arr[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    return False
    
for i in request:
    if (binary_search(i, 0, N - 1)):
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
