
---

## 07 - py_pattern_tracker

**Fichero a entregar:** `pattern_tracker.py`  
**Función permitida:** ninguna en especial

### Enunciado

Escribe una función que cuente cuántas veces dos dígitos consecutivos forman una secuencia creciente de exactamente uno en uno.

```
- Solo considera caracteres adyacentes en la cadena.
- Cuenta pares donde ambos caracteres sean dígitos.
- Incrementa el contador si int(s[i]) == int(s[i-1]) + 1.
- Devuelve el total de pares consecutivos válidos.
```

### Prototipo

```python
def Pattern_tracker(s: str) -> int:
```

### Ejemplos

```
Pattern_tracker("123a345")   → 4   # (1,2), (2,3), (3,4), (4,5)
Pattern_tracker("1a2b3c4d5") → 0   # no hay dígitos adyacentes
Pattern_tracker("")          → 0
Pattern_tracker("111111")    → 0   # no hay secuencia creciente
Pattern_tracker("012345")    → 5
Pattern_tracker("98")        → 0   # decreciente, no cuenta
```

---
