
## 03 - py_bracket_validator

**Fichero a entregar:** `bracket_validator.py`  
**Función permitida:** ninguna en especial

### Enunciado

Escribe una función que determine si una cadena con brackets es válida.

```
Una cadena es válida si:
- Los brackets abiertos son cerrados por el mismo tipo de bracket.
- Los brackets abiertos son cerrados en el orden correcto.
- Cada bracket de cierre tiene su correspondiente bracket de apertura.
- Los caracteres no bracket se ignoran.
```

### Prototipo

```python
def bracket_validator(s: str) -> bool:
```

### Ejemplos

```
bracket_validator("()")                         → True
bracket_validator("()[]{}")                     → True
bracket_validator("{[()]}")                     → True
bracket_validator("")                           → True
bracket_validator("hello(hhhh)world{ho}w are") → True
bracket_validator("(]")                         → False
bracket_validator("([)]")                       → False
bracket_validator("(((")                        → False
bracket_validator("())")                        → False
```
