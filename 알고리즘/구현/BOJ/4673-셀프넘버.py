nums = [x for x in range(1, 10001)]

for i in range(1, 10001):
    dn = i
    for j in str(i):
        dn += int(j)
    if (dn in nums):
        nums.remove(dn)
    
for i in nums:
    print(i)
