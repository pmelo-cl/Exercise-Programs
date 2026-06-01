def Shift_alphabet(s: str, n: int) -> str:

    string = ""
    for c in s:
        if c.isalpha():
            if c.islower():
                string += chr((ord(c) - ord('a') + n) % 26 + ord('a'))
            if c.isupper():
                string += chr((ord(c) - ord('A') + n) % 26 + ord('A'))
        else:
            string += c
    return string


print(Shift_alphabet("abz", 1))           # → "bca"
print(Shift_alphabet("AbZ", 1))           # → "BcA"
print(Shift_alphabet("Hello World!", 3))  # → "Khoor Zruog!"
print(Shift_alphabet("bca", -1))          # → "abz"
print(Shift_alphabet("abc", 26))          # → "abc"
print(Shift_alphabet("xyz", 3))           # → "abc"
print(Shift_alphabet("", 10))             # → ""
print(Shift_alphabet("12345", 4))         # → "12345"
