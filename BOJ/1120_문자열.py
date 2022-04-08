import sys
input = sys.stdin.readline

A, B = input().split()
a = len(A)
b = len(B)
ans = b
for i in range(b-a+1):
    tmp = 0
    for j in range(a):
        if (A[j] != B[j+i]):
            tmp += 1
    ans = min(ans,  tmp)
print(ans)
        
