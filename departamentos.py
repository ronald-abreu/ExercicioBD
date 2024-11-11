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
    id = int(input("ID: "))
    nome = input("Nome do Departamento: ")
    numero = input("Número: ")
    gerente_id = None  # gerente ainda não definido
    departamento = Departamento(id, nome, numero, gerente_id)
    banco['departamentos'].append(departamento)
    print("Departamento cadastrado!")

def atualizar_departamento(banco, id):
    dados_atualizados = {}
    if input("Atualizar Nome? (S/N): ").lower() == "s":
        dados_atualizados["nome"] = input("Novo Nome: ")
    if input("Atualizar Número? (S/N): ").lower() == "s":
        dados_atualizados["numero"] = input("Novo Número: ")
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
