def Anagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)


print(Anagram("racecar", "carrace"))              # → True
print(Anagram("racecar", "carace"))               # → False
print(Anagram("listen", "silent"))                # → True
print(Anagram("hello", "world"))                  # → False
print(Anagram("Conversation", "Voices rant on"))  # → False
print(Anagram("a", "a"))                          # → True
