correo = "cusi@gmail.com"
contrasena = "cusi"
intentos = 0
error=2

correo_u = input("Ingrese su correo electrónico: ")

while intentos < 3:
    contrasena_u = input("Ingrese su contraseña: ")

    if (correo_u == correo and contrasena == contrasena_u):
        print('Bienvenido')
        break
    else:
        intentos += 1
        print("Error en contraseña. Le quedan", error, "intentos.")
        error -= 1 
# --- Aporte de Cruz: Sistema de bloqueo de seguridad ---
if intentos == 3:
    print("Acceso bloqueado. Demasiados intentos fallidos.")