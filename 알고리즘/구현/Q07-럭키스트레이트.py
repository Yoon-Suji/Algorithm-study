import sys
input = sys.stdin.readline

N = input().rstrip()
length = len(N)
left = 0
right = 0
for i in range(0, length // 2):
    left += int(N[i])
    right += int(N[length - i - 1])
if (left == right):
    print('LUCKY')
else: print('READY')
    
