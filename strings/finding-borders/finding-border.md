
# Finding Borders

**Límite de tiempo:** 1.00 s  
**Límite de memoria:** 512 MB

Un *border* (borde) de un string es un prefijo que también es sufijo del string, pero no el string completo. Por ejemplo, los bordes de `abcababcab` son `ab` y `abcab`.

Tu tarea es encontrar todas las longitudes de los bordes de un string dado.

## Input
La única línea de la entrada contiene un string de longitud $n$ compuesto por caracteres de la 'a' a la 'z'.

## Output
Imprime todas las longitudes de los bordes del string en orden creciente.

## Constraints

$1 \leq n \leq 10^6$

---

### Ejemplo

**Input:**
```
abcababcab
```

**Output:**
```
2 5
```