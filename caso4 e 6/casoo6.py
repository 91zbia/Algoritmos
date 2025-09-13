livros = [
    {"livro": "os sete maridos de evelyn hugo", "usuario": "beatriz", "dias": 7},
    {"livro": "jantar secreto", "usuario": "gabriella", "dias": 2},
    {"livro": "harry potter e o cálice de fogo", "usuario": "mariana", "dias": 31},
    {"livro": "diário de um banana", "usuario": "miguel", "dias": 17},
    {"livro": "battle royale", "usuario": "viviane", "dias": 5},
    {"livro": "a culpa é das estrelas", "usuario": "davi", "dias": 10},
    {"livro": "o pequeno princípe", "usuario": "laura", "dias": 3},
    {"livro": "o hobbit", "usuario": "josé", "dias": 12}
]


mais_tempo = max(livros, key=lambda x: x["dias"])
soma = sum(x["dias"] for x in livros)
quantidade = len(livros)
media = soma / quantidade

print(f"lista de empréstimos:")
for e in livros:
    print(f"livro: {e['livro']}, usuário: {e['usuario']}, dias emprestados: {e['dias']}")


print("os livros emprestados há mais de 7 dias são:")
for emp in livros:
    if emp["dias"] > 7:
        print(f"livro: {emp['livro']}, usuário: {emp['usuario']}, dias emprestado: {emp['dias']}")

print("os usuários com livros emprestados são:")
for emp in livros:
    print(f"usuário: {emp['usuario']}")

print(f"livro emprestado há mais tempo ---\n{mais_tempo['livro']}, usuário: {mais_tempo['usuario']}, dias: {mais_tempo['dias']}")
print(f"a média de dias de empréstimo: {media:.2f} dias")
