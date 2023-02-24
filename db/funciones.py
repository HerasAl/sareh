from db.conexionBD import obtener_conexion
import bcrypt
import datetime
import jwt

SECRET_KEY = 'dc7d41b80c1f852a5a5f1d7cdf67cbe5b8e5c3a30b0a5c5f5' # Deberías cambiar esto por una clave segura y única para tu aplicación

def insertUser(usuario, correo, passw):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        # Generamos el hash de la contraseña
        hashed_passw = bcrypt.hashpw(passw.encode('utf-8'), bcrypt.gensalt())
        # Insertamos el usuario en la tabla sh_users
        cursor.execute("INSERT INTO sh_users(user, pwd, correo, fecha_registro) VALUES (%s, %s, %s, NOW())",
                       (usuario, hashed_passw, correo))
    conexion.commit()
    conexion.close()

def logueo(usuario, passw):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT user, pwd FROM sh_users WHERE user = %s", (usuario,))
        row = cursor.fetchone()
        if row is None:
            return None # El usuario no existe
        # Verificamos la contraseña
        hashed_passw = row[1].encode('utf-8') # Convertimos el hash a bytes
        if bcrypt.checkpw(passw.encode('utf-8'), hashed_passw):
            # La contraseña es correcta, generamos el token JWT
            payload = {
                'sub': row[0],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
            return token
        else:
            return None # La contraseña es incorrecta