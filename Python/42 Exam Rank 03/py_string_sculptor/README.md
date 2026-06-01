
---

## 09 - py_string_sculptor

**Fichero a entregar:** `sculptor.py`  
**Función permitida:** ninguna en especial

### Enunciado

Escribe una función que devuelva una cadena donde los caracteres alfabéticos alternen entre minúscula y mayúscula.

```
- Empieza con minúscula en el primer carácter alfabético.
- Alterna entre minúscula/mayúscula en cada letra siguiente.
- Los caracteres no alfabéticos se mantienen igual.
- Los no alfabéticos NO afectan la alternancia.
```

### Prototipo

```python
def sculptor(text: str) -> str:
```

### Ejemplos

```
sculptor("Hello world")    → "hElLo WoRlD"
sculptor("Hello, world!")  → "hElLo, WoRlD!"
sculptor("123abcDEF")      → "123aBcDeF"
sculptor("a-bC-dEf-ghIj")  → "a-Bc-DeF-gHiJ"
sculptor("")               → ""
sculptor("12345")          → "12345"
sculptor("A")              → "a"
sculptor("ab")             → "aB"
```

---
