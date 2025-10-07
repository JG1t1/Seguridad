#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

# Mensaje cifrado
mensaje_cifrado = """

"""

# Frecuencia de letras en español (aproximada)
frecuencia_espanol = "EAOSRNIDLCTUMPBQVGHFJZYXKW"

# Limpiar mensaje: solo letras mayúsculas
mensaje_limpio = ''.join(filter(str.isalpha, mensaje_cifrado.upper()))

# Contar frecuencia de cada letra en el mensaje
frecuencias = Counter(mensaje_limpio)

# Ordenar letras del mensaje por frecuencia (más común a menos común)
orden_cifrado = [letra for letra, _ in frecuencias.most_common()]

# Crear diccionario de reemplazo usando frecuencias
tabla_reemplazo = {}
for i, letra in enumerate(orden_cifrado):
    if i < len(frecuencia_espanol):
        tabla_reemplazo[letra] = frecuencia_espanol[i]
    else:
        tabla_reemplazo[letra] = letra  # letras raras quedan igual

# Función para aplicar descifrado
def descifrar(texto):
    resultado = ""
    for c in texto:
        c_upper = c.upper()
        if c_upper in tabla_reemplazo:
            nueva_letra = tabla_reemplazo[c_upper]
            # Mantener mayúsculas y minúsculas
            resultado += nueva_letra if c.isupper() else nueva_letra.lower()
        else:
            resultado += c
    return resultado

# Descifrar mensaje
mensaje_descifrado = descifrar(mensaje_cifrado)

print("=== Mensaje descifrado (análisis de frecuencias) ===\n")
print(mensaje_descifrado)
