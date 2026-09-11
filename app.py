# app.py — Oficina de Conserto (versão inicial)
from flask import Flask, render_template, request, redirect, url_for, session
import models


class Servico:
    def __init__(self, id, descricao, categoria):
        self.id = id
        self.descricao = descricao
        self.categoria = categoria


app = Flask(__name__)
app.secret_key = "oficina-secreta"


@app.route("/")
def index():
    q = request.args.get("q", "")
    if q:
        lista = [s for s in models.servicos if q.lower() in s["descricao"].lower()]
    else:
        lista = models.servicos
    return render_template("index.html", servicos=lista, q=q,
                           categorias=models.todas_categorias())


@app.route("/servico/<int:servico_id>")
def ver_servico(servico_id):
    servico = models.buscar_servico(servico_id)
    if servico is None:
        return "Serviço não encontrado", 404
    return f"""
    <h2>{servico['descricao']}</h2>
    <p>Categoria: {servico['categoria']}</p>
    <p>Prazo: {servico['prazo']}</p>
    <p>Valor: R$ {servico['valor']}</p>
    <a href='/'>Voltar para a oficina</a>
    """


@app.route("/categoria/<nome>")
def ver_categoria(nome):
    lista = []
    for s in models.servicos:
        if s["categoria"].lower() == nome.lower():
            lista.append(s)
    return render_template("index.html", servicos=lista, q="",
                           categorias=models.todas_categorias())


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        for u in models.usuarios:
            if u["nome"] == request.form["nome"] and u["senha"] == request.form["senha"]:
                session["usuario"] = u["nome"]
                return redirect(url_for("painel"))
        return render_template("login.html", erro="Usuário ou senha inválidos")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)