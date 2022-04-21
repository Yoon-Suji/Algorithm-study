import sys
input = sys.stdin.readline

N = int(input())
arr = list(input().split())

x = 1
y = 1

for i in arr:
    if (i == 'R'):
        if (y < N): y += 1

    elif (i == 'L'):
        if (y > 1): y -= 1

    elif (i == 'U'):
        if (x > 1): x -= 1

    else:
        if (x < N): x += 1
print(x, y)
        
