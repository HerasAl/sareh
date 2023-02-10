from flask import session
from conexionBD import *

def dataLogin():
    info = {
        "id_usr"        :session['id_usr'],
        "usr"           :session['usr'],
        "pass"           :session['pass'],
        "ult_conn"           :session['pass'],
        "id_data"           :session['id_data'],
    }
    return info

def dataPerfilUsuario():
    conexion_MySQLdb = connectionBD() 
    mycursor       = conexion_MySQLdb.cursor(dictionary=True)
    idUser         = session['id']
    
    querySQL  = ("SELECT * FROM sh_users WHERE id='%s'" % (idUser,))
    mycursor.execute(querySQL)
    datosUsuario = mycursor.fetchone() 
    mycursor.close() #cerrrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
    return datosUsuario