'''Autor : Joseph Manuel Jaimes Florez
grupo : j3
Descripcion : Detección de palíndromos
Verifica si una palabra se lee igual al derecho y al revés.

Fecha : 19/07/2025
'''
palabra = input("Escribe una palabra: ").lower()
invertida = palabra[::-1]

if palabra == invertida:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")