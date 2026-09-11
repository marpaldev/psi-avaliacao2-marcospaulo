from flask import Blueprint

servicos_bp = Blueprint("servicos", __name__, template_folder="templates")

from blueprints.servicos import routes