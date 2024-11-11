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


def criar_funcionario(banco):
    while True:
        id = int(input("ID do Funcionário: "))

        if any(funcionario.id == id for funcionario in banco['funcionarios']):
            print("ID já existente. Por favor, insira um ID diferente.")
        else: break

    primeiro_nome = input("Primeiro Nome: ")
    meio_nome = input("Meio Nome: ")
    ultimo_nome = input("Último Nome: ")

    while True:
        cpf = input("CPF: ")

        if any(funcionario.cpf == cpf for funcionario in banco['funcionarios']):
            print("CPF já registrado. Por favor, insira um CPF diferente.")
        else: break

    endereco = input("Endereço: ")
    salario = float(input("Salário: "))
    sexo = input("Sexo: ")
    data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")

    funcionario = Funcionario(id, primeiro_nome, meio_nome, ultimo_nome, cpf, endereco, salario, sexo, data_nascimento)
    banco['funcionarios'].append(funcionario)

    # Perguntar se deseja associar o funcionário a um projeto
    associar = input("Deseja associar este funcionário a um projeto? (S/N): ").strip().lower()
    if associar == 's':
        projeto_id = int(input("ID do Projeto: "))
        if associar_funcionario_a_projeto(banco, funcionario.id, projeto_id):
            print(f"Funcionário {funcionario.primeiro_nome} {funcionario.ultimo_nome} foi associado ao projeto com ID {projeto_id}.")
        else:
            print("Erro ao associar o funcionário ao projeto.")


def atualizar_funcionario(banco, id):
    

            # Procura o funcionário no banco
            funcionario = next((f for f in banco['funcionarios'] if f.id == id), None)
            if funcionario is None:
                print("Funcionário não encontrado!")
                return

            # Pergunta ao usuário se ele deseja atualizar todos os campos
            atualizar_todos = input("Deseja atualizar todos os dados do funcionário? (S/N): ").strip().lower()
            
            if atualizar_todos == 's':
                # Atualiza todos os dados do funcionário
                funcionario.primeiro_nome = input(f"Novo Primeiro Nome (atual: {funcionario.primeiro_nome}): ")
                funcionario.meio_nome = input(f"Novo Meio Nome (atual: {funcionario.meio_nome}): ")
                funcionario.ultimo_nome = input(f"Novo Último Nome (atual: {funcionario.ultimo_nome}): ")
                while True:
                    novo_cpf = input(f"Novo CPF (atual: {funcionario.cpf}): ")

                    if any(funcionario.cpf == novo_cpf and funcionario.id != id for funcionario in banco['funcionarios']):
                        print("CPF já registrado. Por favor, insira um CPF diferente.")
                    else:
                        funcionario.cpf = novo_cpf
                        break

                funcionario.endereco = input(f"Novo Endereço (atual: {funcionario.endereco}): ")
                funcionario.salario = float(input(f"Novo Salário (atual: {funcionario.salario}): "))
                funcionario.sexo = input(f"Novo Sexo (atual: {funcionario.sexo}): ")
                funcionario.data_nascimento = input(f"Nova Data de Nascimento (atual: {funcionario.data_nascimento}): ")

            else:
                # Atualiza apenas os campos selecionados individualmente
                if input("Atualizar Primeiro Nome? (S/N): ").lower() == "s":
                    funcionario.primeiro_nome = input(f"Novo Primeiro Nome (atual: {funcionario.primeiro_nome}): ")
                if input("Atualizar Meio Nome? (S/N): ").lower() == "s":
                    funcionario.meio_nome = input(f"Novo Meio Nome (atual: {funcionario.meio_nome}): ")
                if input("Atualizar Último Nome? (S/N): ").lower() == "s":
                    funcionario.ultimo_nome = input(f"Novo Último Nome (atual: {funcionario.ultimo_nome}): ")
                if input("Atualizar CPF? (S/N): ").lower() == "s":
                    while True:
                        novo_cpf = input(f"Novo CPF (atual: {funcionario.cpf}): ")

                        if any(funcionario.cpf == novo_cpf and funcionario.id != id for funcionario in banco['funcionarios']):
                            print("CPF já registrado. Por favor, insira um CPF diferente.")
                        else:
                            funcionario.cpf = novo_cpf
                            break
                if input("Atualizar Endereço? (S/N): ").lower() == "s":
                    funcionario.endereco = input(f"Novo Endereço (atual: {funcionario.endereco}): ")
                if input("Atualizar Salário? (S/N): ").lower() == "s":
                    funcionario.salario = float(input(f"Novo Salário (atual: {funcionario.salario}): "))
                if input("Atualizar Sexo? (S/N): ").lower() == "s":
                    funcionario.sexo = input(f"Novo Sexo (atual: {funcionario.sexo}): ")
                if input("Atualizar Data de Nascimento? (S/N): ").lower() == "s":
                    funcionario.data_nascimento = input(f"Nova Data de Nascimento (atual: {funcionario.data_nascimento}): ")
            print("Funcionário atualizado com sucesso!")


def deletar_funcionario(banco, id):
    
    for departamento in banco['departamentos']:
        if departamento.gerente and departamento.gerente.id == id:
            departamento.gerente = None  # Remove o funcionário da gerência

            # Remover o funcionário da lista de funcionários
        banco['funcionarios'] = [f for f in banco['funcionarios'] if f.id != id]
        print("Funcionário deletado!")


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
