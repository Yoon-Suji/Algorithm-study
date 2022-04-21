import sys
input = sys.stdin.readline

S = list(input().rstrip())
l = len(S)

left = 0
right = l - 1
add = 0
while (left < right):
    if (S[left] == S[right]):
        left += 1
        right -= 1
    else:
        add += 1
        left = add
        right = l - 1
        
print(l + add)
