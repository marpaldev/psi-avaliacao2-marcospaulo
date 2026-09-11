from flask import render_template, request, session, redirect, url_for
import models
from blueprints.auth import auth_bp

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        for u in models.usuarios:
            if u["nome"] == request.form["nome"] and u["senha"] == request.form["senha"]:
                session["usuario"] = u["nome"]
                return redirect(url_for("servicos.index"))
        return render_template("login.html", erro="Usuário ou senha inválidos")
    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("servicos.index"))