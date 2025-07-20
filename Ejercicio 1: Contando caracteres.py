'''Autor : Joseph Manuel Jaimes Florez
grupo : j3
Descripcion : Conteo de caracteres y espacios
Cuenta cuántos caracteres y espacios hay en una frase.
Fecha : 19/07/2025
'''
frase = input("Escribe una frase: ")
total_caracteres = len(frase)
espacios = frase.count(" ")

print(f"La frase tiene {total_caracteres} caracteres en total.")
print(f"La frase tiene {espacios} espacios.")