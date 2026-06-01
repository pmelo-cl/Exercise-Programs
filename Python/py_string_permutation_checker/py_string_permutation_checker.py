def string_permutation_checker(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    dict1 = {}

    for c in s1:
        dict1[c] = dict1.get(c, 0) + 1
    for c in s2:
        if c not in dict1:
            return False
        dict1[c] -= 1
        if dict1[c] == 0:
            del dict1[c]
    return len(dict1) == 0


print(string_permutation_checker("abc", "bca"))
