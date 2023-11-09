import sys
input = sys.stdin.readline

s = input().rstrip()
alphabet = [0] * 26
num = 0
for i in range(len(s)):
    if not (s[i].isdecimal()):
        alphabet[ord(s[i]) - ord('A')] += 1
    else:
        num += int(s[i])
for i in range(26):
    for _ in range(alphabet[i]):
        print(chr(i + ord('A')), end='')
print(num)
