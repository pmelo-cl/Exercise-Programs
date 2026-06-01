def sculptor(text: str) -> str:
    lower = True
    s = ""
    for c in text:
        if c.isalpha():
            if lower:
                s += c.lower()
            else:
                s += c.upper()
            lower = not lower
        else:
            s += c
    return s


print(sculptor("Hello world"))    # → "hElLo WoRlD"
print(sculptor("Hello, world!"))  # → "hElLo, WoRlD!"
print(sculptor("123abcDEF"))      # → "123aBcDeF"
print(sculptor("a-bC-dEf-ghIj"))  # → "a-Bc-DeF-gHiJ"
print(sculptor(""))               # → ""
print(sculptor("12345"))          # → "12345"
print(sculptor("A"))              # → "a"
print(sculptor("ab"))             # → "aB"
