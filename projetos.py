from funcionarios import associar_funcionario_a_projeto

class Projeto:
    def __init__(self, id, nome, numero, local, departamento_id):
        self.id = id
        self.nome = nome
        self.numero = numero
        self.local = local
        self.departamento_id = departamento_id  # Armazene apenas o ID do departamento

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'numero': self.numero,
            'local': self.local,
            'departamento_id': self.departamento_id  # Apenas o ID do departamento
        }

def criar_projeto(banco):
    while True:
        id = int(input("ID do Projeto: "))

        if any(projeto.id == id for projeto in banco['projetos']):
            print("ID já existente. Por favor, insira um ID diferente.")
        else: break

    while True:
        nome = input("Nome do Projeto: ")

        if any(projeto.nome == nome for projeto in banco['projetos']):
            print("Nome de projeto já existente. Por favor, insira um nome diferente.")
        else: break

    while True:
        numero = input("Número: ")

        if any(projeto.numero == numero for projeto in banco['projetos']):
            print("Número de projeto já existente. Por favor, insira um número novo.")
        else: break
        
    local = input("Local: ")
    departamento_id = int(input("ID do Departamento: "))

    projeto = Projeto(id, nome, numero, local, departamento_id)
    banco['projetos'].append(projeto)

    # Associar o projeto ao departamento
    departamento = next((d for d in banco['departamentos'] if d.id == departamento_id), None)
    if departamento:
        departamento.adicionar_projeto(projeto)
        print(f"Projeto {projeto.nome} associado ao departamento {departamento.nome}!")

    # Perguntar se deseja associar o projeto a um funcionário
    associar = input("Deseja associar este projeto a um funcionário? (S/N): ").strip().lower()
    if associar == 's':
        funcionario_id = int(input("ID do Funcionário: "))
        if associar_funcionario_a_projeto(banco, funcionario_id, projeto.id):
            print(f"Projeto {projeto.nome} foi associado ao funcionário com ID {funcionario_id}.")
        else:
            print("Erro ao associar o projeto ao funcionário.")

def atualizar_projeto(banco, id, **dados_atualizados):
    dados_atualizados = {}
    if input("Atualizar Nome? (S/N): ").lower() == "s":
        while True:
            novo_nome = input("Novo Nome: ")

            if any(projeto.nome == novo_nome and projeto.id != id for projeto in banco['projetos']):
                print("Nome de projeto já existente. Por favor, insira um nome diferente.")
            else:
                dados_atualizados["nome"] = novo_nome
                break

    if input("Atualizar Local? (S/N): ").lower() == "s":
        dados_atualizados["local"] = input("Novo Local: ")
    for projeto in banco['projetos']:
        if projeto.id == id:
            for chave, valor in dados_atualizados.items():
                setattr(projeto, chave, valor)
            print("Projeto atualizado!")

def deletar_projeto(banco, id):
    banco['projetos'] = [p for p in banco['projetos'] if p.id != id]
    # Também precisamos remover o projeto do departamento, caso ele tenha sido associado
    for departamento in banco['departamentos']:
        departamento.projetos = [p for p in departamento.projetos if p.id != id]
    print("Projeto deletado!")
