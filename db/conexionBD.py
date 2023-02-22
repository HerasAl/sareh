import mysql.connector

def connectionBD():
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "heras12345",
        database = "sareh",
    )
    if db:
        return db
    else:
        return None