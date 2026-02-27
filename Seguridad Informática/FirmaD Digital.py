from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# 1. Generar par de claves (RSA)
def generar_claves():
    clave_privada = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    clave_publica = clave_privada.public_key()
    return clave_privada, clave_publica

# 2. Firma del mensaje 
def firmar_mensaje(mensaje, clave_privada):
    firma = clave_privada.sign(
        mensaje.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return firma

# 3. Verificar la firma 
def verificar_firma(mensaje, firma, clave_publica):
    try:
        clave_publica.verify(
            firma,
            mensaje.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False


# 4. Prueba del sistema 
# Generar claves
clave_privada, clave_publica = generar_claves()

# Mensaje original
mensaje = "La firma digital es un mecanismo criptográfico equivalente a " \
"la firma manuscrita que garantiza la autenticidad, integridad y no repudio."

# Firmar mensaje
firma = firmar_mensaje(mensaje, clave_privada)

print("Mensaje original:")
print(mensaje)

print("\nFirma digital generada:")
print(firma)

# Verificar firma correcta
resultado = verificar_firma(mensaje, firma, clave_publica)
print("\n¿Firma válida?", resultado)

# 5. MODIFICAR MENSAJE
mensaje_modificado = "La firma digital garantiza seguridad totl"

resultado_modificado = verificar_firma(mensaje_modificado, firma, clave_publica)
print("\nMensaje modificado:")
print(mensaje_modificado)

print("\n¿Firma válida tras modificar el mensaje?", resultado_modificado)