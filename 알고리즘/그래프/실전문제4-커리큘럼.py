import sys
from collections import deque
import copy
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
time = [0] * (N+1)
indegree = [0] * (N+1)
for i in range(1, N+1):
    curri = list(map(int, input().split()))
    time[i] = curri[0]
    for j in curri[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    for i in range(1, N+1):
        if (indegree[i] == 0): q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], time[i] + result[now])
            indegree[i] -= 1
            if (indegree[i] == 0):
                q.append(i)
    
    for i in result[1:]:
        print(i)
        
topology_sort()
