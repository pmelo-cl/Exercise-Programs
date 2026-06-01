def cryptic_sorter(tlist: list) -> list:

    def count_vowels(string: str) -> int:
        vowels = "aeiouAEIOU"
        count = 0
        for c in string:
            if c in vowels:
                count += 1
        return count

    return sorted(tlist, key=lambda x: (
        count_vowels(x),
        len(x),
        x.lower()
        ))


print(cryptic_sorter(["apple", "bat", "car", "ae", "b"]))   # → ['b', 'bat', 'car', 'ae', 'apple']
print(cryptic_sorter(["dog", "cat", "hi", "a"]))            # → ['a', 'hi', 'cat', 'dog']
print(cryptic_sorter(["bat", "cat", "ant"]))                # → ['ant', 'bat', 'cat']
print(cryptic_sorter(["bbb", "ccc", "ddd"]))                # → ['bbb', 'ccc', 'ddd']
print(cryptic_sorter([]))                                   # → []
