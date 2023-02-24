from flask import Flask, render_template, url_for
from flask import request

from asistente import sentidos
from module import musica
from db.funciones import insertUser, logueo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

#APIS DE CONTROL DE USUARIOS

@app.route("/reg", methods=['POST'])
def alta():
    data = request.json
    insertUser(data.get('name'),data.get('email'),data.get('password'))
    return ({'status':1})

@app.route("/goin", methods=['POST'])
def login():
    data = request.json
    ok = logueo(data.get('usr'),data.get('password'))
    if ok is not None:
        return ({
            'code':1,
            'tkn':ok
        })
    else:
        return({'msg': "tas mal chavito"})