# models.py — Camada Model da Oficina de Conserto (dados em memória)

class Servico:
    def __init__(self, id, descricao, categoria):
        self.id = id
        self.descricao = descricao
        self.categoria = categoria

usuarios = [
    {"id": 1, "nome": "admin", "senha": "1234"},
]

servicos = [
    {"id": 1, "descricao": "Troca de tela do celular", "categoria": "Eletrônico", "prazo": "3 dias úteis", "valor": 250.00},
    {"id": 2, "descricao": "Calibragem de bicicleta", "categoria": "Mecânico", "prazo": "1 dia útil", "valor": 80.00},
    {"id": 3, "descricao": "Reparo de placa-mãe", "categoria": "Eletrônico", "prazo": "5 dias úteis", "valor": 450.00},
    {"id": 4, "descricao": "Instalação de interruptor", "categoria": "Elétrico", "prazo": "2 dias úteis", "valor": 120.00},
    {"id": 5, "descricao": "Conserto de ventilador", "categoria": "Elétrico", "prazo": "2 dias úteis", "valor": 90.00},
]


def buscar_servico(servico_id):
    for s in servicos:
        if s["id"] == servico_id:
            return s
    return None


def buscar_por_categoria(categoria):
    return [s for s in servicos if s["categoria"].lower() == categoria.lower()]


def buscar_por_descricao(parte):
    return [s for s in servicos if parte.lower() in s["descricao"].lower()]


def todas_categorias():
    categorias = []
    for s in servicos:
        if s["categoria"] not in categorias:
            categorias.append(s["categoria"])
    return categorias