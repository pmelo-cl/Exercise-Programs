## 10 - py_twist_sequence

**Fichero a entregar:** `twist_sequence.py`  
**Función permitida:** ninguna en especial

### Enunciado

Escribe una función que rote una lista `n` posiciones hacia la derecha.

```
- Desplaza los elementos n posiciones a la derecha.
- Los elementos que superan el final vuelven al inicio.
- Valores negativos de n rotan hacia la izquierda.
- Devuelve la nueva lista rotada.
```

### Prototipo

```python
def twister(nums: list, n: int) -> list:
```

### Ejemplos

```
twister([1, 2, 3, 4, 5], 2)     → [4, 5, 1, 2, 3]
twister([4, 2, 1, -1, 'a'], 4)  → [2, 1, -1, 'a', 4]
twister([1, 2, 3], 3)           → [1, 2, 3]
twister([1, 2, 3], 5)           → [2, 3, 1]
twister([1, 2, 3, 4], -1)       → [2, 3, 4, 1]
twister([], 3)                  → []
twister([1], 10)                → [1]
```
