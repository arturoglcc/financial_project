import bcrypt

# Hash almacenado en la base de datos
stored_hash = b"$2b$12$z.C8/j6IrpbdSV4IakLzH.198czi8YIsrJNa2Au7LCCccrBDN0avS"

# Contraseña que se usó originalmente
password = "1"  # Reemplaza este valor

# Verificación
if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
    print("El hash es válido y la contraseña coincide.")
else:
    print("El hash no es válido o la contraseña no coincide.")
