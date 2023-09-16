# Función para contar caracteres
def contar_caracteres(texto):
    # Utiliza la función len() para contar los caracteres en el texto
    return len(texto)

# Solicita al usuario que ingrese un texto
texto = input("Ingrese el texto que desea contar: ")

# Llama a la función contar_caracteres y muestra el resultado
numero_de_caracteres = contar_caracteres(texto)
print(f"Número de caracteres: {numero_de_caracteres}")