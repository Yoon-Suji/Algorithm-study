import sys
input = sys.stdin.readline

N = int(input())
top = list(map(int, input().split()))
st = [(top[-1], N-1)]
ans = [0] * N
for i in range(N-2, -1, -1):
    while st:
        if (st[-1][0] > top[i]):
            break
        if (st[-1][0] <= top[i]):
            ans[st[-1][1]] = i+1
            st.pop()
    st.append((top[i], i))
print(*ans)
