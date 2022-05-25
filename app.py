from flask import Flask, render_template, g
import sqlite3

app = Flask("hello")
app.config.from_object(__name__)

def connect_bd():
    return sqlite3.connect(database)

@app.before_request
def antes_requisicao():
    g.bd = conecta_bd()

@app.teardown_request
def depois_requisicao(e):
    g.bd.close()


DATABASE = banco.bd
SECRET_KEY = "chave"

@app.route("/")
def exibir_entradas():
    sql = "SELECT titulo, texto FROM entradas"
    nome = "nezi"
    return render_template("hello.html", nome_pessoa=name)

