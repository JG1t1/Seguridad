import sys
# necesario un texto.txt con el texto que se desea cambiar
# Verificar si se proporcionaron los parámetros correctos
if len(sys.argv) != 3:
    print("Uso: python modificar_texto.py <letra_a_cambiar> <letra_a_reemplazar>")
    sys.exit(1)

letra_a_cambiar = sys.argv[1]
letra_a_reemplazar = sys.argv[2]

# Leer el contenido actual del archivo de texto
with open('texto.txt', 'r') as archivo:
    texto = archivo.read()

# Realizar el reemplazo de la letra
texto_modificado = texto.replace(letra_a_cambiar, letra_a_reemplazar)

# Escribir el texto modificado de nuevo en el archivo
with open('texto.txt', 'w') as archivo:
    archivo.write(texto_modificado)

print(f'Se ha cambiado la letra "{letra_a_cambiar}" por "{letra_a_reemplazar}" en el archivo "texto.txt".')
