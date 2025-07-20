'''Autor : Joseph Manuel Jaimes Florez
grupo : j3
Descripcion : Contador de vocales en una frase
Cuenta cuántas vocales hay en total, tanto mayúsculas como minúsculas.
Fecha : 19/07/2025
'''
frase = input("Escribe una frase: ")

a = frase.count("a") + frase.count("A")
e = frase.count("e") + frase.count("E")
i = frase.count("i") + frase.count("I")
o = frase.count("o") + frase.count("O")
u = frase.count("u") + frase.count("U")

total_vocales = a + e + i + o + u

print(f"La frase tiene {total_vocales} vocales.")