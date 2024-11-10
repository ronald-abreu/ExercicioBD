class Projeto:
    def __init__(self, id, nome, numero, local):
        self.id = id
        self.nome = nome
        self.numero = numero
        self.local = local

    def to_dict(self):
        return vars(self)

def criar_projeto(banco, **dados):
    banco['projetos'].append(Projeto(**dados))

def atualizar_projeto(banco, id, **dados_atualizados):
    for projeto in banco['projetos']:
        if projeto.id == id:
            for chave, valor in dados_atualizados.items():
                setattr(projeto, chave, valor)
            return True
    return False

def deletar_projeto(banco, id):
    banco['projetos'] = [p for p in banco['projetos'] if p.id != id]
