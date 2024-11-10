import json
from funcionarios import Funcionario
from departamentos import Departamento
from projetos import Projeto

def inicializar_banco_dados():
    return {'funcionarios': [], 'departamentos': [], 'projetos': []}

def salvar_em_arquivo(banco, nome_arquivo):
    dados = {
        'funcionarios': [f.to_dict() for f in banco['funcionarios']],
        'departamentos': [d.to_dict() for d in banco['departamentos']],
        'projetos': [p.to_dict() for p in banco['projetos']]
    }
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def carregar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            return {
                'funcionarios': [Funcionario(**f) for f in dados['funcionarios']],
                'departamentos': [
                    Departamento(**d, gerente=Funcionario(**d['gerente'])) for d in dados['departamentos']
                ],
                'projetos': [Projeto(**p) for p in dados['projetos']]
            }
    except FileNotFoundError:
        return inicializar_banco_dados()
