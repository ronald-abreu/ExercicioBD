from banco import inicializar_banco_dados, salvar_em_arquivo, carregar_arquivo
from funcionarios import criar_funcionario, atualizar_funcionario, deletar_funcionario, associar_funcionario_a_projeto, desassociar_funcionario_de_projeto
from departamentos import criar_departamento, atualizar_departamento, deletar_departamento
from projetos import criar_projeto, atualizar_projeto, deletar_projeto



if __name__ == "__main__":
    banco = inicializar_banco_dados()
    
    # Exemplo de criação de dados
    criar_funcionario(banco, id=1, primeiro_nome='João', meio_nome='D', ultimo_nome='Silva', 
                      cpf='123.456.789-00', endereco='Rua 1, 123', salario=3000, sexo='M', data_nascimento='01/01/1990')
    criar_funcionario(banco, id=2, primeiro_nome='Maria', meio_nome='A', ultimo_nome='Costa', 
                      cpf='987.654.321-00', endereco='Rua 2, 456', salario=3500, sexo='F', data_nascimento='02/02/1985')

    criar_departamento(banco, id=1, nome='TI', numero='001', gerente=banco['funcionarios'][0])
    criar_departamento(banco, id=2, nome='RH', numero='002', gerente=banco['funcionarios'][1])

    criar_projeto(banco, id=1, nome='Desenvolvimento Sistema', numero='101', local='São Paulo')
    criar_projeto(banco, id=2, nome='Treinamento Funcional', numero='102', local='Rio de Janeiro')
    criar_projeto(banco, id=3, nome='Sistema Novo', numero='103', local='Ceara')

    associar_funcionario_a_projeto(banco, 1, 1)
    associar_funcionario_a_projeto(banco, 2, 2)
    associar_funcionario_a_projeto(banco, 1, 3)

    salvar_em_arquivo(banco, 'empresa.json')

    atualizar_funcionario(banco, 1, salario=3500)
    #deletar_departamento(banco, 1)

    #deletar_funcionario(banco, 1)  

    salvar_em_arquivo(banco, 'empresa.json')
