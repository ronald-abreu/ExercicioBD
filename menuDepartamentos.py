# Alteração para atualizar o gerente com o objeto Funcionario correspondente
from banco import salvar_em_arquivo
from departamentos import *


def menu_departamentos(banco):
    while True:
        print("\n--- Menu Departamentos ---")
        print("1. Cadastrar Departamento")
        print("2. Atualizar Departamento")
        print("3. Deletar Departamento")
        print("4. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            criar_departamento(banco)
            salvar_em_arquivo(banco, 'empresa.json')
            break
        elif opcao == "2":
            id = int(input("ID do Departamento a atualizar: "))
            atualizar_departamento(banco, id)
            salvar_em_arquivo(banco, 'empresa.json')
            break
        elif opcao == "3":
            id = int(input("ID do Departamento a deletar: "))
            deletar_departamento(banco, id)
            salvar_em_arquivo(banco, 'empresa.json')
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        salvar_em_arquivo(banco, 'empresa.json')
