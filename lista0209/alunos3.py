turma = {

    "aluno1" : { 
        "ellie":  6.7
    },

    "aluno2" : {
        "joel": 8.5
    },
    
    "aluno3": {
        "dina": 9.0
    }
}

print(f"nota do aluno 1:{turma.get("aluno1").get("ellie")}")
turma.pop("aluno2")
print(turma)