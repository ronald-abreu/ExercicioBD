from banco import salvar_em_arquivo
from departamentos import Departamento
from funcionarios import *



def menu_funcionarios(banco):
    while True:
        print("\n--- Menu Funcionários ---")
        print("1. Cadastrar Funcionário")
        print("2. Atualizar Funcionário")
        print("3. Deletar Funcionário")
        print("4. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            if not banco['departamentos']:
                print("Antes de cadastrar, crie pelo menos um departamento.")
                continue
            # Cadastro de funcionário
            criar_funcionario(banco)

            # Salvar no arquivo
            salvar_em_arquivo(banco, 'empresa.json')
            break
            
        elif opcao == "2":
            # Solicita o ID do funcionário a ser atualizado
            id = int(input("ID do Funcionário a atualizar: "))
            atualizar_funcionario(banco, id)
            # Salva as alterações no arquivo JSON
            salvar_em_arquivo(banco, 'empresa.json')
            
            break
        elif opcao == "3":
            id = int(input("ID do Funcionário a deletar: "))
    
            # Remover o funcionário da gerência de qualquer departamento onde ele seja o gerente
            deletar_funcionario(banco, id)
            salvar_em_arquivo(banco, 'empresa.json')
            break
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        salvar_em_arquivo(banco, 'empresa.json')
