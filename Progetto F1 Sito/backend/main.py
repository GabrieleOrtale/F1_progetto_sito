from flask import Flask, render_template, request #per installare flask pip install flask
import mysql.connector
app = Flask(__name__)
def crea_connessione():
    db_conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "f1_race"
    )
    return db_conn
@app.route('/')
def index():
    db_conn = crea_connessione()
    cursor = db_conn.cursor()
    cursor.execute('SELECT * FROM piloti')
    piloti = cursor.fetchall()#fetchall prende tutte le righe
    db_conn.close()
    return render_template('index.html',piloti= piloti) #render_template è una funzionalità di Flask e genera una pagina prendendo come esempio index.html