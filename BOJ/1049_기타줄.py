import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cost = []
for _ in range(M):
    cost.append(list(map(int, input().split())))

package = sorted(cost, key = lambda x:(x[0]))
one = sorted(cost, key = lambda x:(x[1]))

package_min = package[0][0]
one_min = one[0][1]

ans = 0
if (N<=6):
    ans = min(package_min, one_min*N)
else:
    if (package_min / 6.0 < one_min):
        ans = N // 6 * package_min
        N %= 6
        ans += min(package_min, one_min*N)
    else:
        ans = one_min * N
print(ans)
