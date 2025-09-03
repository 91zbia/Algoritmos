def aula():
    dias = ["segunda", "terça", "quarta", "quinta", "sexta"]
    presencas = {}
    for dia in dias:
        presentes = input(f"quem estave no {dia}?\n -")
        listapresenca = [nome.strip() for nome in presentes.split(",")]
        for nome in listapresenca:
            if nome in presencas:
                presencas[nome] += 1
            else:
                presencas[nome] = 1

    tododias = [nome for nome, count in presencas.items() if count == len(dias)]
    faltaumdia = [nome for nome, count in presencas.items() if count < len(dias)]

    print(f"alunos presentes todos os dias: {', '.join(tododias)}")
    print(f"alunos que faltaram pelo menos um dia: {', '.join(faltaumdia)}")
    
aula()