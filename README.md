## ❇**Taller Guiado: Trabajando con Cadenas de Caracteres en Python**

Este taller está diseñado para practicar el uso de cadenas de caracteres en Python. Cada ejercicio tiene instrucciones claras y una explicación de cómo resolverlo.

------

### **Objetivo del taller**

- Aprender a manipular, validar y formatear cadenas de caracteres.
- Usar los métodos básicos de las cadenas para resolver problemas prácticos.

------

### **Ejercicio 1: Contando caracteres**

#### **Instrucción:**

Escribe un programa que solicite al usuario una frase y muestre:

1. La cantidad total de caracteres en la frase.
2. La cantidad de espacios en la frase.

#### **Guía:**

1. Usa `len()` para contar el total de caracteres.
2. Usa el método `count()` para contar los espacios.

#### **Código base:**

```python
frase = input("Escribe una frase: ")
total_caracteres = len(frase)
espacios = frase.count(" ")

print(f"La frase tiene {total_caracteres} caracteres en total.")
print(f"La frase tiene {espacios} espacios.")
```

DESCRIPCION 

Esto lo que hace es contar cuántos caracteres hay en total (incluye todo, hasta espacios) y cuántos espacios hay en esa frase.
 Usamos `len()` para contar todo y `count(" ")` para contar los espacios. Es útil para revisar texto o analizar frases.

------

### **Ejercicio 2: Validando nombres**

#### **Instrucción:**

Crea un programa que solicite al usuario su nombre completo y verifique:

1. Que solo contenga letras.
2. Que comience con mayúscula.

#### **Guía:**

1. Usa `isalpha()` para verificar que solo hay letras.
2. Usa `istitle()` para verificar que las palabras comiencen con mayúscula.

#### **Código base:**

```python
nombre = input("Escribe tu nombre completo: ")

if nombre.replace(" ", "").isalpha():
    if nombre.istitle():
        print("El nombre es válido.")
    else:
        print("El nombre debe comenzar con mayúscula.")
else:
    print("El nombre solo debe contener letras.")
```

DESCRIPCION

Acá se pide el nombre y se revisa que solo tenga letras (sin números ni símbolos) y que empiece con mayúsculas.
 Se usa `replace()` para ignorar espacios, `isalpha()` para ver si son letras, y `istitle()` para ver si cada palabra empieza en mayúscula.

------

### **Ejercicio 3: Invirtiendo palabras**

#### **Instrucción:**

Escribe un programa que pida al usuario una palabra y muestre la palabra invertida.

#### **Guía:**

1. Usa el operador de slicing `[::-1]` para invertir la cadena.

#### **Código base:**

```python
palabra = input("Escribe una palabra: ")
invertida = palabra[::-1]
print(f"La palabra invertida es: {invertida}")
```

DESCRIPCION

Se escribe una palabra y el programa la voltea.
 Usa `[::-1]` que es como decir “dámela al revés”. Sirve para juegos, curiosidades o palíndromos.

------

### **Ejercicio 4: Cifrando texto**

#### **Instrucción:**

Crea un programa que solicite al usuario una frase y reemplace todas las vocales por un carácter especial (*).

#### **Guía:**

1. Usa `replace()` repetidamente para reemplazar las vocales.
2. Asegúrate de manejar tanto mayúsculas como minúsculas.

#### **Código base:**

```python
frase = input("Escribe una frase: ")

frase_cifrada = frase.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*")
frase_cifrada = frase_cifrada.replace("A", "*").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*")

print(f"La frase cifrada es: {frase_cifrada}")
```

DESCRIPCION

Esto reemplaza todas las vocales por `*` para ocultarlas. Se usa `replace()` una y otra vez. Sirve para ocultar información o hacer cifrados simples.

------

### **Ejercicio 5: Contador de vocales**

#### **Instrucción:**

Escribe un programa que cuente cuántas vocales hay en una frase ingresada por el usuario.

#### **Guía:**

1. Usa `count()` para contar las vocales individualmente.
2. Suma los resultados.

#### **Código base:**

```python
frase = input("Escribe una frase: ")

a = frase.count("a") + frase.count("A")
e = frase.count("e") + frase.count("E")
i = frase.count("i") + frase.count("I")
o = frase.count("o") + frase.count("O")
u = frase.count("u") + frase.count("U")

total_vocales = a + e + i + o + u

print(f"La frase tiene {total_vocales} vocales.")
```

DESCRIPCION

Este código cuenta cuántas veces aparece cada vocal (tanto minúscula como mayúscula).
 Usamos `count()` muchas veces, una por cada vocal. Luego sumamos todo para saber cuántas hay en total. Sirve para análisis de texto o curiosidad.

------

### **Ejercicio 6: Formateando cadenas**

#### **Instrucción:**

Escribe un programa que tome un número de teléfono ingresado por el usuario (10 dígitos) y lo formatee como `(XXX) XXX-XXXX`.

#### **Guía:**

1. Usa slicing para dividir la cadena en partes.
2. Usa `f-strings` o concatenación para formatear.

#### **Código base:**

```python
telefono = input("Escribe un número de teléfono de 10 dígitos: ")
if len(telefono) == 10 and telefono.isdigit():
    telefono_formateado = f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}"
    print(f"El número formateado es: {telefono_formateado}")
else:
    print("El número debe tener exactamente 10 dígitos.")
```

DESCRIPCION

Esto toma un número (como 3204567890) y lo convierte a un formato más bonito: (320) 456-7890.
 Se usa `slicing` (dividir por partes) y `f-string` para que quede con paréntesis y guion. Verifica que el número tenga 10 dígitos exactos.

------

### **Ejercicio 7: Detectando palíndromos**

#### **Instrucción:**

Escribe un programa que determine si una palabra ingresada por el usuario es un palíndromo (se lee igual al derecho y al revés).

#### **Guía:**

1. Usa slicing para invertir la palabra.
2. Compara la palabra original con la invertida.

#### **Código base:**

```python
palabra = input("Escribe una palabra: ").lower()
invertida = palabra[::-1]

if palabra == invertida:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
```

DESCRIPCION

Esto revisa si una palabra se lee igual al derecho y al revés.
 Convierte todo a minúsculas con `.lower()` y la invierte con `[::-1]`. Luego compara si son iguales. Es útil para juegos de palabras.
