## 08 - py_shadow_merge

**Fichero a entregar:** `shadow_merge.py`  
**Función permitida:** `sorted()`

### Enunciado

Escribe una función que fusione dos listas de enteros y devuelva el resultado ordenado de menor a mayor.

```
- Combina todos los elementos de ambas listas.
- Maneja listas vacías o None correctamente.
- Devuelve una nueva lista ordenada en orden ascendente.
```

### Prototipo

```python
def mergeList(list1: list, list2: list) -> list:
```

### Ejemplos

```
mergeList([1, 3, 5, -1], [0, 8, 2, 1]) → [-1, 0, 1, 1, 2, 3, 5, 8]
mergeList([99, -22, 10, 9], [])         → [-22, 9, 10, 99]
mergeList(None, [5, 3, 1])              → [1, 3, 5]
mergeList([7, 6, 8], None)              → [6, 7, 8]
mergeList([], [])                       → []
mergeList([1, 1, 1], [1, 1])            → [1, 1, 1, 1, 1]
mergeList([-5, -2], [-3, -1])           → [-5, -3, -2, -1]
```
