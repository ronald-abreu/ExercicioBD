# Alteração para atualizar o gerente com o objeto Funcionario correspondente
from banco import salvar_em_arquivo
from departamentos import Departamento
from funcionarios import Funcionario

def menu_departamentos(banco):
    while True:
        print("\n--- Menu Departamentos ---")
        print("1. Cadastrar Departamento")
        print("2. Atualizar Departamento")
        print("3. Deletar Departamento")
        print("4. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            id = int(input("ID: "))
            nome = input("Nome do Departamento: ")
            numero = input("Número: ")
            gerente_id = None  # gerente ainda não definido
            departamento = Departamento(id, nome, numero, gerente_id)
            banco['departamentos'].append(departamento)
            print("Departamento cadastrado!")
        elif opcao == "2":
            id = int(input("ID do Departamento a atualizar: "))
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
                    break
        elif opcao == "3":
            id = int(input("ID do Departamento a deletar: "))
            banco['departamentos'] = [d for d in banco['departamentos'] if d.id != id]
            print("Departamento deletado!")
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        salvar_em_arquivo(banco, 'empresa.json')
