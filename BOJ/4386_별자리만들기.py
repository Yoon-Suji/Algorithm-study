import sys
input = sys.stdin.readline

def dist(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def find(x):
    if x == parent[x]:
        return x
    return find(parent[x])

def union(x, y):
    x = find(x)
    y = find(y)
    if (x<y):
        parent[y] = x
    else:
        parent[x] = y

n = int(input())
star = []
for _ in range(n):
    x, y = map(float, input().split())
    star.append([x, y])

cost = []
parent = [i for i in range(n)]

for i in range(n):
    for j in range(i+1, n):
        d = dist(star[i][0], star[i][1], star[j][0], star[j][1])
        cost.append([d, i, j])
cost.sort()

ans = 0
for d, x, y in cost:

    if (find(x) != find(y)):
        union(x, y)
        ans += d

print(round(ans, 2))


