
---

## 05 - py_mirror_matrix

**Fichero a entregar:** `mirror_matrix.py`  
**Función permitida:** ninguna en especial

### Enunciado

Escribe una función que invierta completamente una matriz 2D como si estuviera aplanada.

```
- Invierte el orden de todos los elementos de la matriz.
- Preserva las dimensiones originales (filas y columnas).
- Devuelve una nueva matriz con los elementos en orden inverso.
```

### Prototipo

```python
def reverseMatrix(s: list) -> list:
```

### Ejemplos

```
reverseMatrix([[1, 2], [3, 4]])           → [[4, 3], [2, 1]]
reverseMatrix([[1, 2, 3], [4, 5, 6]])     → [[6, 5, 4], [3, 2, 1]]
reverseMatrix([[1, 2, 3, 4]])            → [[4, 3, 2, 1]]
reverseMatrix([[1], [2], [3]])           → [[3], [2], [1]]
reverseMatrix([[1]])                     → [[1]]
reverseMatrix([])                        → []
reverseMatrix([[1,2,3],[4,5,6],[7,8,9]]) → [[9,8,7],[6,5,4],[3,2,1]]
```

---
