from banco import inicializar_banco_dados, salvar_em_arquivo, carregar_arquivo
from menuFuncionarios import menu_funcionarios
from menuDepartamentos import menu_departamentos
from menuProjetos import menu_projetos

banco = carregar_arquivo('empresa.json')

def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Menu Funcionários")
        print("2. Menu Departamentos")
        print("3. Menu Projetos")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            if not banco['departamentos']:
                print("Antes de cadastrar um funcionário, crie pelo menos um departamento.")
                continue
            menu_funcionarios(banco)
        elif opcao == "2":
            menu_departamentos(banco)
        elif opcao == "3":
            menu_projetos(banco)
        elif opcao == "4":
            print("Saindo...")
            salvar_em_arquivo(banco, 'empresa.json')
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
