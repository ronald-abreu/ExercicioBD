from banco import salvar_em_arquivo
from departamentos import Departamento
from funcionarios import Funcionario, associar_funcionario_a_projeto


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
                print("Antes de cadastrar um funcionário, crie pelo menos um departamento.")
                continue
            # Cadastro de funcionário
            id = int(input("ID do Funcionário: "))
            primeiro_nome = input("Primeiro Nome: ")
            meio_nome = input("Meio Nome: ")
            ultimo_nome = input("Último Nome: ")
            cpf = input("CPF: ")
            endereco = input("Endereço: ")
            salario = float(input("Salário: "))
            sexo = input("Sexo: ")
            data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")

            funcionario = Funcionario(id, primeiro_nome, meio_nome, ultimo_nome, cpf, endereco, salario, sexo, data_nascimento)
            banco['funcionarios'].append(funcionario)

            # Perguntar se deseja associar o funcionário a um projeto
            associar = input("Deseja associar este funcionário a um projeto? (S/N): ").strip().lower()
            if associar == 's':
                projeto_id = int(input("ID do Projeto: "))
                if associar_funcionario_a_projeto(banco, funcionario.id, projeto_id):
                    print(f"Funcionário {funcionario.primeiro_nome} {funcionario.ultimo_nome} foi associado ao projeto com ID {projeto_id}.")
                else:
                    print("Erro ao associar o funcionário ao projeto.")

            # Salvar no arquivo
            salvar_em_arquivo(banco, 'empresa.json')
            break
            
        elif opcao == "2":
            # Solicita o ID do funcionário a ser atualizado
            id = int(input("ID do Funcionário a atualizar: "))

            # Procura o funcionário no banco
            funcionario = next((f for f in banco['funcionarios'] if f.id == id), None)
            if funcionario is None:
                print("Funcionário não encontrado!")
                return

            # Pergunta ao usuário se ele deseja atualizar todos os campos
            atualizar_todos = input("Deseja atualizar todos os dados do funcionário? (S/N): ").strip().lower()
            
            if atualizar_todos == 's':
                # Atualiza todos os dados do funcionário
                funcionario.primeiro_nome = input(f"Novo Primeiro Nome (atual: {funcionario.primeiro_nome}): ")
                funcionario.meio_nome = input(f"Novo Meio Nome (atual: {funcionario.meio_nome}): ")
                funcionario.ultimo_nome = input(f"Novo Último Nome (atual: {funcionario.ultimo_nome}): ")
                funcionario.cpf = input(f"Novo CPF (atual: {funcionario.cpf}): ")
                funcionario.endereco = input(f"Novo Endereço (atual: {funcionario.endereco}): ")
                funcionario.salario = float(input(f"Novo Salário (atual: {funcionario.salario}): "))
                funcionario.sexo = input(f"Novo Sexo (atual: {funcionario.sexo}): ")
                funcionario.data_nascimento = input(f"Nova Data de Nascimento (atual: {funcionario.data_nascimento}): ")

            else:
                # Atualiza apenas os campos selecionados individualmente
                if input("Atualizar Primeiro Nome? (S/N): ").lower() == "s":
                    funcionario.primeiro_nome = input(f"Novo Primeiro Nome (atual: {funcionario.primeiro_nome}): ")
                if input("Atualizar Meio Nome? (S/N): ").lower() == "s":
                    funcionario.meio_nome = input(f"Novo Meio Nome (atual: {funcionario.meio_nome}): ")
                if input("Atualizar Último Nome? (S/N): ").lower() == "s":
                    funcionario.ultimo_nome = input(f"Novo Último Nome (atual: {funcionario.ultimo_nome}): ")
                if input("Atualizar CPF? (S/N): ").lower() == "s":
                    funcionario.cpf = input(f"Novo CPF (atual: {funcionario.cpf}): ")
                if input("Atualizar Endereço? (S/N): ").lower() == "s":
                    funcionario.endereco = input(f"Novo Endereço (atual: {funcionario.endereco}): ")
                if input("Atualizar Salário? (S/N): ").lower() == "s":
                    funcionario.salario = float(input(f"Novo Salário (atual: {funcionario.salario}): "))
                if input("Atualizar Sexo? (S/N): ").lower() == "s":
                    funcionario.sexo = input(f"Novo Sexo (atual: {funcionario.sexo}): ")
                if input("Atualizar Data de Nascimento? (S/N): ").lower() == "s":
                    funcionario.data_nascimento = input(f"Nova Data de Nascimento (atual: {funcionario.data_nascimento}): ")

            # Salva as alterações no arquivo JSON
            salvar_em_arquivo(banco, 'empresa.json')
            print("Funcionário atualizado com sucesso!")
            break
        elif opcao == "3":
            id = int(input("ID do Funcionário a deletar: "))
    
            # Remover o funcionário da gerência de qualquer departamento onde ele seja o gerente
            for departamento in banco['departamentos']:
                if departamento.gerente and departamento.gerente.id == id:
                    departamento.gerente = None  # Remove o funcionário da gerência

            # Remover o funcionário da lista de funcionários
            banco['funcionarios'] = [f for f in banco['funcionarios'] if f.id != id]
            print("Funcionário deletado!")
            salvar_em_arquivo(banco, 'empresa.json')
            break
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        salvar_em_arquivo(banco, 'empresa.json')
