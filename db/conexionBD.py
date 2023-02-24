import pymysql


def obtener_conexion():

    try:
        conexion = pymysql.connect(
            host='192.168.0.103',
            user='root',
            password='heras12345',
            db='sareh'
        )
        print("Conectados")
        return conexion
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error: ", e)