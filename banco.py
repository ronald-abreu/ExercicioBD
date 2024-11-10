import json
from funcionarios import Funcionario
from departamentos import Departamento
from projetos import Projeto

def inicializar_banco_dados():
    return {'funcionarios': [], 'departamentos': [], 'projetos': []}

def salvar_em_arquivo(banco, nome_arquivo):
    dados = {
        'funcionarios': [f.to_dict() for f in banco['funcionarios']],
        'departamentos': [d.to_dict() for d in banco['departamentos']],  # Converte todos os departamentos
        'projetos': [p.to_dict() for p in banco['projetos']]  # Converte todos os projetos
    }

    # Salvando os dados no arquivo
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
        
def carregar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)

            # Lista de campos esperados para cada classe
            campos_funcionario = Funcionario.__init__.__code__.co_varnames[1:]
            campos_departamento = Departamento.__init__.__code__.co_varnames[1:]
            campos_projeto = Projeto.__init__.__code__.co_varnames[1:]

            return {
                'funcionarios': [
                    Funcionario(**{key: f[key] for key in campos_funcionario if key in f})
                    for f in dados['funcionarios']
                ],
                'departamentos': [
                    Departamento(
                        **{key: d[key] for key in campos_departamento if key in d and key != 'gerente'},
                        gerente=Funcionario(**{key: d['gerente'][key] for key in campos_funcionario if key in d['gerente']}) if d['gerente'] else None
                    )
                    for d in dados['departamentos']
                ],
                'projetos': [
                    Projeto(**{key: p[key] for key in campos_projeto if key in p})
                    for p in dados['projetos']
                ]
            }
    except FileNotFoundError:
        return inicializar_banco_dados()
