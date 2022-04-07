import sys
input = sys.stdin.readline

cost = int(input())

money = 1000 - cost
coins = [500, 100, 50, 10, 5, 1]
ans = 0
for coin in coins:
    ans += money // coin
    money %= coin
print(ans)
