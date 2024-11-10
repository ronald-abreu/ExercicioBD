from banco import salvar_em_arquivo
from projetos import Projeto
from departamentos import Departamento

def menu_projetos(banco):
    while True:
        print("\n--- Menu Projetos ---")
        print("1. Cadastrar Projeto")
        print("2. Atualizar Projeto")
        print("3. Deletar Projeto")
        print("4. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            id = int(input("ID: "))
            nome = input("Nome do Projeto: ")
            numero = input("Número: ")
            local = input("Local: ")
            departamento_id = int(input("ID do Departamento: "))  # ID do departamento, não o objeto inteiro

            # Criar o projeto com o ID do departamento
            projeto = Projeto(id, nome, numero, local, departamento_id)

            # Associar o projeto ao departamento
            departamento = next((d for d in banco['departamentos'] if d.id == departamento_id), None)
            if departamento:
                departamento.adicionar_projeto(projeto)
                banco['projetos'].append(projeto)
                print("Projeto cadastrado e associado ao departamento!")
            else:
                print("Departamento não encontrado!")
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
