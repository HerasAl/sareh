from flask import Flask, render_template
from flask import request

from asistente import sentidos
from module import musica

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    #objeto = sentidos.oido()
    #comando = objeto.escuchar()
    return render_template("init.html")

@app.route('/login', methods=['GET'])
def log():
    return render_template("login.html")

@app.route('/registrar', methods=['GET'])
def reg():
    return render_template("register.html")

@app.route("/music", methods=['POST'])
def media():
    return musica.music(request.form['song'])

@app.route("/down", methods=['POST'])
def down():
    return musica.downSave(request.json)
    