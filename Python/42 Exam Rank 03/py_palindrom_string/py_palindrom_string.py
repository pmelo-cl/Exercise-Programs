def isPalindrome(s: str) -> bool:
    if not s or s == "":
        return True
    p = ""
    for c in s:
        if c.isalnum():
            p += c.lower()
    return p == p[::-1]


print(isPalindrome("madam"))                           # → True
print(isPalindrome("racecar"))                         # → True
print(isPalindrome("A man, a plan, a canal: Panama"))  # → True
print(isPalindrome("No 'x' in Nixon"))                 # → True
print(isPalindrome(""))                                # → True
print(isPalindrome("hello"))                           # → False
print(isPalindrome("12321"))                           # → True
print(isPalindrome("12345"))                           # → False
print(isPalindrome("Able was I ere I saw Elba"))       # → True
