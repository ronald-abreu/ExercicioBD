import json

class Funcionario:
    def __init__(self, id, primeiro_nome, meio_nome, ultimo_nome, cpf, endereco, salario, sexo, data_nascimento):
        self.id = id
        self.primeiro_nome = primeiro_nome
        self.meio_nome = meio_nome
        self.ultimo_nome = ultimo_nome
        self.cpf = cpf
        self.endereco = endereco
        self.salario = salario
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.projetos = []  # Lista para armazenar IDs dos projetos associados

    def to_dict(self):
        return {**vars(self), 'projetos': self.projetos}


def criar_funcionario(banco, **dados):
    banco['funcionarios'].append(Funcionario(**dados))


def atualizar_funcionario(banco, id, **dados_atualizados):
    for funcionario in banco['funcionarios']:
        if funcionario.id == id:
            for chave, valor in dados_atualizados.items():
                setattr(funcionario, chave, valor)
            return True
    return False


def deletar_funcionario(banco, id):
    
    for departamento in banco['departamentos']:
        if departamento.gerente.id == id:
            departamento.gerente = None  

    
    banco['funcionarios'] = [f for f in banco['funcionarios'] if f.id != id]



def listar_funcionarios(banco):
    return [funcionario.to_dict() for funcionario in banco['funcionarios']]


def buscar_funcionario_por_id(banco, id):
    for funcionario in banco['funcionarios']:
        if funcionario.id == id:
            return funcionario.to_dict()
    return None


def buscar_funcionario_por_cpf(banco, cpf):
    for funcionario in banco['funcionarios']:
        if funcionario.cpf == cpf:
            return funcionario.to_dict()
    return None


def associar_funcionario_a_projeto(banco, funcionario_id, projeto_id):
    funcionario = next((f for f in banco['funcionarios'] if f.id == funcionario_id), None)
    if funcionario:
        # Verifica se o ID do projeto já está associado ao funcionário
        if projeto_id not in funcionario.projetos:
            funcionario.projetos.append(projeto_id)
            return True
    return False


def desassociar_funcionario_de_projeto(banco, funcionario_id, projeto_id):
    funcionario = next((f for f in banco['funcionarios'] if f.id == funcionario_id), None)
    if funcionario and projeto_id in funcionario.projetos:
        funcionario.projetos.remove(projeto_id)
        return True
    return False
