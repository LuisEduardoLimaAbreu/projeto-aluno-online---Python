lista_principal = []  

while True:
    print("Selecione uma opcao:")
    print("1 - Cadastrar Aluno")
    print("2 - Relatorio Estudantil")
    print("3 - Remover Aluno")
    print("0 - Sair")

    opcao = int(input())

    if opcao == 1:
        lista_aluno = [] 
        nome = input("Nome do aluno: ")
        matricula = input("Matricula do aluno: ")
        idade = int(input("Idade do aluno: "))
        curso = input("Curso do aluno: ")
        horario = input("Horario do curso: ")
        lista_aluno.extend([nome, matricula, idade, curso, horario])
        lista_principal.append(lista_aluno)
        print("Aluno cadastrado com sucesso!")

    elif opcao == 2:
        if len(lista_principal) == 0:
            print("Nao ha alunos cadastrados.")
        else:
            print("Relatorio Estudantil:")
            for aluno in lista_principal:
                print("Nome: {}, Matricula: {}, Idade: {}, Curso: {}, Horário: {}"
                      .format(aluno[0], aluno[1], aluno[2], aluno[3], aluno[4]))

    elif opcao == 3:
        if len(lista_principal) == 0:
            print("Nao ha alunos cadastrados.")
        else:
            matricula = input("Digite a matricula do aluno a ser removido: ")
            removido = False
            for aluno in lista_principal:
                if aluno[1] == matricula:
                    lista_principal.remove(aluno)
                    removido = True
                    print("Aluno removido com sucesso!")
                    break
            if not removido:
                print("Aluno nao encontrado.")

    elif opcao == 0:
        print("Encerrando o programa...")
        break

    else:
        print("Opcao invalida. Tente novamente.")




















