from banco import salvar_em_arquivo
from projetos import Projeto
from departamentos import Departamento
from funcionarios import associar_funcionario_a_projeto

def menu_projetos(banco):
    while True:
        print("\n--- Menu Projetos ---")
        print("1. Cadastrar Projeto")
        print("2. Atualizar Projeto")
        print("3. Deletar Projeto")
        print("4. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            id = int(input("ID do Projeto: "))
            nome = input("Nome do Projeto: ")
            numero = input("Número: ")
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


        elif opcao == "2":
            id = int(input("ID do Projeto a atualizar: "))
            dados_atualizados = {}
            if input("Atualizar Nome? (S/N): ").lower() == "s":
                dados_atualizados["nome"] = input("Novo Nome: ")
            if input("Atualizar Local? (S/N): ").lower() == "s":
                dados_atualizados["local"] = input("Novo Local: ")
            for projeto in banco['projetos']:
                if projeto.id == id:
                    for chave, valor in dados_atualizados.items():
                        setattr(projeto, chave, valor)
                    print("Projeto atualizado!")
                    break
        elif opcao == "3":
            id = int(input("ID do Projeto a deletar: "))
            banco['projetos'] = [p for p in banco['projetos'] if p.id != id]
            # Também precisamos remover o projeto do departamento, caso ele tenha sido associado
            for departamento in banco['departamentos']:
                departamento.projetos = [p for p in departamento.projetos if p.id != id]
            print("Projeto deletado!")
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        salvar_em_arquivo(banco, 'empresa.json')
