turma = {

    "personagem1" : { 
        "nome":"ellie",
        "nota":"6,7"
    },

    "personagem2" : {
        "nome":"joel",
        "nota":"8,5"
    }

}

print(f"primeiro aluno: {turma.get("personagem1").get("nome")}")
print(f"primeiro aluno: {turma.get("personagem2").get("nota")}")