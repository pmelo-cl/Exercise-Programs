
## 02 - py_base_converter

**Fichero a entregar:** `convertBase.py`  
**Función permitida:** `int()`

### Enunciado

Escribe una función que convierta un número representado como string desde una base origen a una base destino.

```
- Soporta bases del 2 al 36.
- Acepta dígitos '0-9' y letras 'A-Z' (sin distinguir mayúsculas).
- Preserva el valor correcto durante la conversión.
- Devuelve "0" si el número de entrada es cero.
- Devuelve "ERROR" si la entrada es inválida.
```

### Prototipo

```python
def convert_base(num: str, from_base: int, to_base: int) -> str:
```

### Ejemplos

```
convert_base("1010", 2, 10)   → "10"
convert_base("10", 10, 2)     → "1010"
convert_base("1A", 16, 10)    → "26"
convert_base("26", 10, 16)    → "1A"
convert_base("ZZZ", 36, 10)   → "46655"
convert_base("0", 10, 2)      → "0"
convert_base("000", 2, 10)    → "0"
convert_base("2", 2, 10)      → "ERROR"
convert_base("G", 16, 10)     → "ERROR"
```
