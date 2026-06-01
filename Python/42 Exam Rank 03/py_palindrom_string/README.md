
## 06 - py_palindrom_string

**Fichero a entregar:** `PalindromString.py`  
**Función permitida:** ninguna en especial

### Enunciado

Escribe una función que determine si una cadena es un palíndromo.

```
- Ignora diferencias entre mayúsculas y minúsculas (A == a).
- Ignora todos los caracteres no alfanuméricos.
- Devuelve True si es palíndromo, False en caso contrario.
```

### Prototipo

```python
def isPalindrome(s: str) -> bool:
```

### Ejemplos

```
isPalindrome("madam")                          → True
isPalindrome("racecar")                        → True
isPalindrome("A man, a plan, a canal: Panama") → True
isPalindrome("No 'x' in Nixon")                → True
isPalindrome("")                               → True
isPalindrome("hello")                          → False
isPalindrome("12321")                          → True
isPalindrome("12345")                          → False
isPalindrome("Able was I ere I saw Elba")      → True
```
