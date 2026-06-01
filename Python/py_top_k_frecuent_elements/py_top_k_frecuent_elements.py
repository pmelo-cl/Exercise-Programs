def k_frecuent_elements(numbers: list[int], k: int) -> list[int]:
    nums = {}

    for n in numbers:
        if n not in nums:
            nums[n] = 1
        elif n in nums:
            nums[n] += 1

    return (list(nums.values())[-k:])


print(k_frecuent_elements([1, 2, 2, 3, 3, 3], 2))  # -> [2, 3]
