def evento():
    palestra = ["beatriz", "gabriella", "filipe", "julia"]
    workshop = ["gabriella", "josué", "beatriz", "flávio"]
    mesaredonda = ["gabriella", "laura", "miguel", "mauro"]
    
    todosparticipantes = set(palestra) | set(workshop) | set(mesaredonda)
    todasatividades = set(palestra) & set(workshop) & set(mesaredonda)
    umatividade = (set(palestra) ^ set(workshop)) ^ set(mesaredonda)
    
    print(f"quem participou de todas as atividades: {', '.join(todasatividades)}")
    print(f"quem participou apenas de uma atividade: {', '.join(umatividade)}")
    print(f"todos os participantes únicos: {', '.join(todosparticipantes)}")
    print(f"número total de participantes distintos: {len(todosparticipantes)}")

evento()