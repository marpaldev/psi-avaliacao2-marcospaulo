# Este arquivo ainda não é usado pela aplicação.
from blueprints.servicos import servicos_bp
from flask import render_template, request, session, redirect, url_for
import models


@servicos_bp.route("/")
def index():
    q = request.args.get("q", "")
    if q:
        lista = [s for s in models.servicos if q.lower() in s["descricao"].lower()]
    else:
        lista = models.servicos
    return render_template("servicos/index.html", servicos=lista, q=q,
                           categorias=models.todas_categorias())

@servicos_bp.route("/servicos")
def listar_servicos():
    return render_template("servicos/index.html", servicos=models.servicos)

@servicos_bp.route("/servico/<int:servico_id>")
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


@servicos_bp.route("/categoria/<nome>")
def ver_categoria(nome):
    lista = []
    for s in models.servicos:
        if s["categoria"].lower() == nome.lower():
            lista.append(s)
    return render_template("servicos/index.html", servicos=lista, q="",
                           categorias=models.todas_categorias())
