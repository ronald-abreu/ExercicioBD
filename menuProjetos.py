from banco import salvar_em_arquivo
from projetos import *

def menu_projetos(banco):
    while True:
        print("\n--- Menu Projetos ---")
        print("1. Cadastrar Projeto")
        print("2. Atualizar Projeto")
        print("3. Deletar Projeto")
        print("4. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            criar_projeto(banco)
            salvar_em_arquivo(banco, 'empresa.json')
            break


        elif opcao == "2":
            id = int(input("ID do Projeto a atualizar: "))
            atualizar_projeto(banco, id)

            salvar_em_arquivo(banco, 'empresa.json')

            break
        elif opcao == "3":
            id = int(input("ID do Projeto a deletar: "))
            deletar_projeto(banco, id)

            salvar_em_arquivo(banco, 'empresa.json')
            break
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        salvar_em_arquivo(banco, 'empresa.json')
