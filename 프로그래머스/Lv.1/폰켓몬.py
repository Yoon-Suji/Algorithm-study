def solution(nums):
    arr = set(nums)
    if (len(arr) > len(nums)/2): return len(nums)/2
    return len(arr)
