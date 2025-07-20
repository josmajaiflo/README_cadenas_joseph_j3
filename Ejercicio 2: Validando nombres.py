'''Autor : Joseph Manuel Jaimes Florez
grupo : j3
Descripcion : Validación de nombre completo
Verifica que el nombre tenga solo letras y comience con mayúscula.
Fecha : 19/07/2025
'''
nombre = input("Escribe tu nombre completo: ")

if nombre.replace(" ", "").isalpha():
    if nombre.istitle():
        print("El nombre es válido.")
    else:
        print("El nombre debe comenzar con mayúscula.")
else:
    print("El nombre solo debe contener letras.")