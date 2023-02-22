from flask import Flask, render_template, url_for
from flask import request

from asistente import sentidos
from module import musica

app = Flask(__name__)
app.secret_key='dc7d41b80c1f852a5a5f1d7cdf67cbe5b8e5c3a30b0a5c5f5'

@app.errorhandler(404)
def not_found():
    if 'conectado' in session:
        return redirect(url_for('inicio'))
    else:
        return render_template("login.html")

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