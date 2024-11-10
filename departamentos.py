from funcionarios import Funcionario

class Departamento:
    def __init__(self, id, nome, numero, gerente):
        self.id = id
        self.nome = nome
        self.numero = numero
        self.gerente = gerente
        self.projetos = []

    def adicionar_projeto(self, projeto):
        self.projetos.append(projeto)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'numero': self.numero,
            'gerente': self.gerente.to_dict() if self.gerente else None,  # Conversão do gerente para dicionário
            'projetos': [p.id for p in self.projetos]  # Aqui, você deve armazenar apenas o ID dos projetos
        }
    
    
def criar_departamento(banco, id, nome, numero, gerente):
    banco['departamentos'].append(Departamento(id, nome, numero, gerente))

def atualizar_departamento(banco, id, **dados_atualizados):
    for departamento in banco['departamentos']:
        if departamento.id == id:
            for chave, valor in dados_atualizados.items():
                setattr(departamento, chave, valor)
            return True
    return False

def deletar_departamento(banco, id):
    banco['departamentos'] = [d for d in banco['departamentos'] if d.id != id]
