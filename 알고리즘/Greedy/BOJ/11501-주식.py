import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = sorted(list(enumerate(arr)), reverse=True, key = lambda x : x[1])
    ans = 0
    before = 0
    for i in range(N):
        if (sorted_arr[i][0] > before):
            for j in range(before, sorted_arr[i][0]):
                ans += sorted_arr[i][1] - arr[j]
        if (before < sorted_arr[i][0] + 1):
            before = sorted_arr[i][0] + 1
        if (before >= N): break
    print(ans)
