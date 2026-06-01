def mergeList(list1: list, list2: list) -> list:

    if not list1:
        return sorted(list2)

    if not list2:
        return sorted(list1)

    list1.extend(list2)
    return sorted(list1)


print(mergeList([1, 3, 5, -1], [0, 8, 2, 1]))  # → [-1, 0, 1, 1, 2, 3, 5, 8]
print(mergeList([99, -22, 10, 9], []))         # → [-22, 9, 10, 99]
print(mergeList(None, [5, 3, 1]))              # → [1, 3, 5]
print(mergeList([7, 6, 8], None))              # → [6, 7, 8]
print(mergeList([], []))                       # → []
print(mergeList([1, 1, 1], [1, 1]))            # → [1, 1, 1, 1, 1]
print(mergeList([-5, -2], [-3, -1]))           # → [-5, -3, -2, -1]
