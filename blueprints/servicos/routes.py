# Este arquivo ainda não é usado pela aplicação.
from app import app
from flask import render_template
import models


@app.route("/servicos")
def listar_servicos():
    return render_template("servicos/index.html", servicos=models.servicos)