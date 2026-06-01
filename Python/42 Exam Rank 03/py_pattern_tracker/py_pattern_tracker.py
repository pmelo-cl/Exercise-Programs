def Pattern_tracker(s: str) -> int:

    count = 0
    for i in range(1, len(s)):
        if s[i].isdigit() and s[i - 1].isdigit():
            if int(s[i]) - int(s[i - 1]) == 1:
                count += 1
    return count


print(Pattern_tracker("123a345"))    # → 4   # (1,2), (2,3), (3,4), (4,5)
print(Pattern_tracker("1a2b3c4d5"))  # → 0   # no hay dígitos adyacentes
print(Pattern_tracker(""))           # → 0
print(Pattern_tracker("111111"))     # → 0   # no hay secuencia creciente
print(Pattern_tracker("012345"))     # → 5
print(Pattern_tracker("98"))         # → 0   # decreciente, no cuenta
