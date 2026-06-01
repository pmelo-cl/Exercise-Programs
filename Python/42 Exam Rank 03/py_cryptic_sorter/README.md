## 04 - py_cryptic_sorter

**Fichero a entregar:** `cryptic_sorter.py`  
**Función permitida:** `sorted()`

### Enunciado

Escribe una función que ordene una lista de cadenas según múltiples criterios.

```
Criterios de ordenación (en orden de prioridad):
1. Por número de vocales (ascendente).
2. Si empatan, por longitud de la cadena (ascendente).
3. Si siguen empatando, orden lexicográfico (alfabético).

Las vocales son: a, e, i, o, u (sin distinguir mayúsculas).
```

### Prototipo

```python
def cryptic_sorter(tlist: list) -> list:
```

### Ejemplos

```
cryptic_sorter(["apple", "bat", "car", "ae", "b"]) → ['b', 'bat', 'car', 'ae', 'apple']
cryptic_sorter(["dog", "cat", "hi", "a"])           → ['a', 'hi', 'cat', 'dog']
cryptic_sorter(["bat", "cat", "ant"])               → ['ant', 'bat', 'cat']
cryptic_sorter(["bbb", "ccc", "ddd"])               → ['bbb', 'ccc', 'ddd']
cryptic_sorter([])                                  → []
