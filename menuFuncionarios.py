from banco import salvar_em_arquivo
from departamentos import Departamento
from funcionarios import Funcionario

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
            id = int(input("ID: "))
            primeiro_nome = input("Primeiro Nome: ")
            meio_nome = input("Meio Nome: ")
            ultimo_nome = input("Último Nome: ")
            cpf = input("CPF: ")
            endereco = input("Endereço: ")
            salario = float(input("Salário: "))
            sexo = input("Sexo (M/F): ")
            data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
            banco['funcionarios'].append(Funcionario(id, primeiro_nome, meio_nome, ultimo_nome, cpf, endereco, salario, sexo, data_nascimento))
            print("Funcionário cadastrado!")
            
        elif opcao == "2":
            id = int(input("ID do Funcionário a atualizar: "))
            dados_atualizados = {}
            if input("Atualizar Primeiro Nome? (S/N): ").lower() == "s":
                dados_atualizados["primeiro_nome"] = input("Novo Primeiro Nome: ")
            if input("Atualizar Salário? (S/N): ").lower() == "s":
                dados_atualizados["salario"] = float(input("Novo Salário: "))
            for funcionario in banco['funcionarios']:
                if funcionario.id == id:
                    for chave, valor in dados_atualizados.items():
                        setattr(funcionario, chave, valor)
                    print("Funcionário atualizado!")
                    break
        elif opcao == "3":
            id = int(input("ID do Funcionário a deletar: "))
            banco['funcionarios'] = [f for f in banco['funcionarios'] if f.id != id]
            print("Funcionário deletado!")
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        salvar_em_arquivo(banco, 'empresa.json')
