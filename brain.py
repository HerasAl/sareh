from flask import Flask
from asistente import sentidos

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    objeto = sentidos.oido()
    return  objeto.escuchar()