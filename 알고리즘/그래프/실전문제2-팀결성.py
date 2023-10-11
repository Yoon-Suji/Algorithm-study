import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parents = [i for i in range(N+1)]

def find_parent(x, parents):
    if (parents[x] != x):
        parents[x] = find_parent(parents[x], parents)
    return parents[x]
    
def union(a, b, parents):
    a = find_parent(a, parents)
    b = find_parent(b, parents)
    if (a < b): parents[b] = a
    else: parents[a] = b
    
for _ in range(M):
    x, a, b = map(int, input().split())
    if (x == 0):
        union(a, b, parents)
    else:
        if (find_parent(a, parents) == find_parent(b, parents)): print('YES')
        else: print('NO')
        
