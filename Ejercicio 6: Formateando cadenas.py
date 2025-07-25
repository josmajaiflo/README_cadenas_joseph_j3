'''Autor : Joseph Manuel Jaimes Florez
grupo : j3
Descripcion : Formato de número telefónico
Convierte un número de 10 dígitos en formato de teléfono 
Fecha : 19/07/2025
'''
telefono = input("Escribe un número de teléfono de 10 dígitos: ")
if len(telefono) == 10 and telefono.isdigit():
    telefono_formateado = f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}"
    print(f"El número formateado es: {telefono_formateado}")
else:
    print("El número debe tener exactamente 10 dígitos.")