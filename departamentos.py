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
    
    
def criar_departamento(banco):
    while True:
        id = int(input("ID: "))

        if any(departamento.id == id for departamento in banco['departamentos']):
            print("ID já existente. Por favor, insira um ID diferente.")
        else: break

    while True:
        nome = input("Nome do Departamento: ")

        if any(departamento.nome == nome for departamento in banco['departamentos']):
            print("Nome de departamento já existente. Por favor, insira um nome diferente.")
        else: break
    
    while True:
        numero = input("Número: ")

        if any(departamento.numero == numero for departamento in banco['departamentos']):
            print("Número de departamento já existente. Por favor, insira um número diferente.")
        else: break

    gerente_id = None  # gerente ainda não definido
    departamento = Departamento(id, nome, numero, gerente_id)
    banco['departamentos'].append(departamento)
    print("Departamento cadastrado!")

def atualizar_departamento(banco, id):
    dados_atualizados = {}
    if input("Atualizar Nome? (S/N): ").lower() == "s":
        while True:
            novo_nome = input("Novo Nome: ")

            if any(departamento.nome == novo_nome and departamento.id != id for departamento in banco['departamentos']):
                print("Nome de departamento já existente. Por favor, insira um nome diferente.")
            else:
                dados_atualizados["nome"] = novo_nome
                break

    if input("Atualizar Número? (S/N): ").lower() == "s":
        while True:
            novo_numero = input("Novo Número: ")

            if any(departamento.numero == novo_numero and departamento.id != id for departamento in banco['departamentos']):
                print("Número de departamento já existente. Por favor, insira um número diferente.")
            else:
                dados_atualizados["numero"] = novo_numero
                break
            
    if input("Atualizar Gerente? (S/N): ").lower() == "s":
        gerente_id = int(input("Novo Gerente (ID do Funcionário): "))
        gerente = next((f for f in banco['funcionarios'] if f.id == gerente_id), None)
        if gerente:
            dados_atualizados["gerente"] = gerente
        else:
            print("Gerente não encontrado!")
    for departamento in banco['departamentos']:
        if departamento.id == id:
            for chave, valor in dados_atualizados.items():
                setattr(departamento, chave, valor)
            print("Departamento atualizado!")

def deletar_departamento(banco, id):
    banco['departamentos'] = [d for d in banco['departamentos'] if d.id != id]
    print("Departamento deletado!")
