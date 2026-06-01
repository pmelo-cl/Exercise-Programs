def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = {}
    for s in strs:
        # Ordenar la cadena para obtener la clave única del anagrama
        key = ''.join(sorted(s))
        # Si la clave no existe, crear una nueva lista vacía
        if key not in groups:
            groups[key] = []
        # Agregar la cadena original al grupo correspondiente
        groups[key].append(s)
    # Devolver solo los valores (las listas de anagramas)
    return sorted(list(groups.values()), key=lambda x: len(x))


print(group_anagrams(["act", "pots", "tops", "cat", "stop", "hat"]))  # -> [["hat"],["act", "cat"],["stop", "pots", "tops"]]
