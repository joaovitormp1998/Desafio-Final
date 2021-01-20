from application import app
from flask import render_template, request
import json
from application.model.dao.PessoaDAO import PessoaDAO

@app.route("/")
def home():
    pessoas = PessoaDAO().get_pessoas()
    return render_template('index.html', pessoas = pessoas)