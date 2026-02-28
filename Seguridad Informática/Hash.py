# AUTENTICACIÓN CON HASH Y SAL
# SHA-256
import hashlib
import os
#Tenemos una base de datos simulada
usuarios_db = {}

def generar_sal():
    """
    Genera una sal aleatoria de 16 bytes
    """
    return os.urandom(16)


def hash_con_sal(password, sal):
    """
    Genera un hash SHA-256 usando contraseña + sal
    """
    password_bytes = password.encode()
    hash_resultado = hashlib.sha256(sal + password_bytes).hexdigest()
    return hash_resultado

#El usuario se registra
def registrar_usuario(usuario, password):
    if usuario in usuarios_db:
        print("El usuario ya existe.")
        return

    sal = generar_sal()
    hash_password = hash_con_sal(password, sal)

    usuarios_db[usuario] = {
        "sal": sal,
        "hash": hash_password
    }

    print(f"Usuario '{usuario}' registrado correctamente.")

# Se inicia sesión 
def iniciar_sesion(usuario, password):
    if usuario not in usuarios_db:
        print("Usuario no encontrado.")
        return

    sal = usuarios_db[usuario]["sal"]
    hash_guardado = usuarios_db[usuario]["hash"]
    hash_ingresado = hash_con_sal(password, sal)

    if hash_ingresado == hash_guardado:
        print("Inicio de sesión exitoso.")
    else:
        print("Contraseña incorrecta.")


# Probamos el código con los usuarios registrados
# Registro
registrar_usuario("Daniela", "gonzalez.4087")

# Login correcto
iniciar_sesion("Daniela", "gonzalez.4087")

# Login incorrecto
iniciar_sesion("Daniela", "gonzalez.4078")