from flask import Flask
from flask import request


from asistente import sentidos
from module import musica

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    #objeto = sentidos.oido()
    #comando = objeto.escuchar()
    return "hola"

@app.route("/music", methods=['POST'])
def media():
    return musica.music(request.form['song'])

@app.route("/down", methods=['POST'])
def down():
    return musica.downSave(request.json)
    