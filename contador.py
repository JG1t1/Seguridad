# Leer el contenido del archivo de texto
with open('texto.txt', 'r') as archivo:
    texto = archivo.read()

# Crear un diccionario para contar las apariciones de cada letra
apariciones = {}

# Recorrer el texto y contar las apariciones de cada letra
for letra in texto:
    if letra.isalpha():
        letra = letra.lower()  # Convertir la letra a minúscula
        if letra in apariciones:
            apariciones[letra] += 1
        else:
            apariciones[letra] = 1

# Convertir el diccionario en una lista de tuplas (letra, apariciones)
lista_apariciones = [(letra, contador) for letra, contador in apariciones.items()]

# Ordenar la lista por apariciones en orden descendente
lista_apariciones.sort(key=lambda x: x[1], reverse=True)

# Imprimir las apariciones de cada letra
for letra, contador in lista_apariciones:
    print(f'{letra}: {contador}')
