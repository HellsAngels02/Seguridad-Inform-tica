#Criptografía Clásica y Moderna
def cifrar_cesar(texto, clave):
    """
    Cifra un texto usando el cifrado César
    """
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nuevo_caracter = chr((ord(caracter) - base + clave) % 26 + base)
            resultado += nuevo_caracter
        else:
            resultado += caracter

    return resultado

def descifrar_cesar(texto_cifrado, clave):
    """
    Descifra un texto usando el cifrado César
    """
    return cifrar_cesar(texto_cifrado, -clave)

def fuerza_bruta_cesar(texto_cifrado):
    """
    Muestra todas las combinaciones posibles
    probando las 26 claves del cifrado César
    """
    print("\nATAQUE DE FUERZA BRUTA:\n")
    for clave in range(26):
        posible_texto = descifrar_cesar(texto_cifrado, clave)
        print(f"Clave {clave}: {posible_texto}")

nombre = "Daniela Alejandra Gonzalez Dionicio"
frase = "Mamma mia es la mejor pelicula musical"
clave = 3

print("CIFRADO CÉSAR \n")

# Cifrado
nombre_cifrado = cifrar_cesar(nombre, clave)
frase_cifrada = cifrar_cesar(frase, clave)

print("Nombre original:", nombre)
print("Nombre cifrado:", nombre_cifrado)

print("\nFrase original:", frase)
print("Frase cifrada:", frase_cifrada)

# Descifrado
print("\nDESCIFRADO\n")
print("Nombre descifrado:", descifrar_cesar(nombre_cifrado, clave))
print("Frase descifrada:", descifrar_cesar(frase_cifrada, clave))

# Ataque de fuerza bruta
fuerza_bruta_cesar(frase_cifrada)
