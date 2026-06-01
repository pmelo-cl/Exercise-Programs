def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return sorted([seen[complement], i])
        seen[num] = i
    return []


print(two_sum([3, 4, 5, 6], 7))  # -> [0,1]
