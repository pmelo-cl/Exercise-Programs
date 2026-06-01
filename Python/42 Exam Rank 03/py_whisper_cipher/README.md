
## 11 - py_whisper_cipher

**Fichero a entregar:** `whisper_cipher.py`  
**Función permitida:** `ord()`, `chr()`

### Enunciado

Escribe una función que aplique un cifrado César desplazando cada carácter alfabético `n` posiciones en el alfabeto.

```
- Preserva mayúsculas y minúsculas por separado.
- Da la vuelta al alfabeto (ej: 'z' + 1 → 'a').
- Los caracteres no alfabéticos se mantienen sin cambios.
- Soporta desplazamientos positivos y negativos.
```

### Prototipo

```python
def Shift_alphabet(s: str, n: int) -> str:
```

### Ejemplos

```
Shift_alphabet("abz", 1)          → "bca"
Shift_alphabet("AbZ", 1)          → "BcA"
Shift_alphabet("Hello World!", 3) → "Khoor Zruog!"
Shift_alphabet("bca", -1)         → "abz"
Shift_alphabet("abc", 26)         → "abc"
Shift_alphabet("xyz", 3)          → "abc"
Shift_alphabet("", 10)            → ""
Shift_alphabet("12345", 4)        → "12345"
```
