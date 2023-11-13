import sys
import itertools
input = sys.stdin.readline
INF = 10**9

N = int(input())
nums = list(map(int, input().split()))
operations = list(map(int, input().split()))
operation = []
for i in range(4):
    for _ in range(operations[i]):
        operation.append(i)

ops = list(itertools.permutations(operation, N-1))

min_ans = INF
max_ans = -INF

for operation in ops:
    st = [nums[0]]
    for i in range(1, N):
        a = st.pop()
        b = nums[i]
        op = operation[i-1]
        if (op == 0): st.append(a+b)
        elif (op == 1): st.append(a-b)
        elif (op == 2): st.append(a*b)
        else: 
            if (a < 0 and b > 0):
                st.append(abs(a) // b * -1)
            else:
                st.append(a//b)
    ans = st.pop()
    min_ans = min(min_ans, ans)
    max_ans = max(max_ans, ans)

print(max_ans)
print(min_ans)
            
