#Criptografía Clásica y Moderna
def cifrar_cesar(texto, clave):
    """
    Cifra un texto usando el cifrado César
    """
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():
            #Aquí determinamos si es mayúscula o minúscula
            base = ord('A') if caracter.isupper() else ord('a')
            #Por lo que aplicamos un desplazamiento 
            nuevo_caracter = chr((ord(caracter) - base + clave) % 26 + base)
            resultado += nuevo_caracter
        else:
            #Por ende mantenemos espacios y símbolos
            resultado += caracter

    return resultado

def descifrar_cesar(texto_cifrado, clave):
    """
    Descifra un texto usando el cifrado César
    """
    return cifrar_cesar(texto_cifrado, -clave)

#Añadimos la fuerza bruta
def fuerza_bruta_cesar(texto_cifrado):
    """
    Muestra todas las combinaciones posibles
    probando las 26 claves del cifrado César
    """
    print("\nATAQUE DE FUERZA BRUTA:\n")
    for clave in range(26):
        posible_texto = descifrar_cesar(texto_cifrado, clave)
        print(f"Clave {clave}: {posible_texto}")

#Añadimos los datos de prueba con un nombre y una frase y la clave
nombre = "Daniela Alejandra Gonzalez Dionicio"
frase = "Mamma mia es la mejor película musical"
clave = 8

print("CIFRADO CÉSAR \n")

# En esta parte ciframos
nombre_cifrado = cifrar_cesar(nombre, clave)
frase_cifrada = cifrar_cesar(frase, clave)

print("Nombre original:", nombre)
print("Nombre cifrado:", nombre_cifrado)

print("\nFrase original:", frase)
print("Frase cifrada:", frase_cifrada)

# Para después descifrar    
print("\nDESCIFRADO\n")
print("Nombre descifrado:", descifrar_cesar(nombre_cifrado, clave))
print("Frase descifrada:", descifrar_cesar(frase_cifrada, clave))

# Por lo que finalizamos con un ataque de fuerza bruta
fuerza_bruta_cesar(frase_cifrada)
