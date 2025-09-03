def biblioteca():
    livros = [
        ["os sete maridos de evelyn hugo", "beatriz", 7],
        ["jantar secreto", "gabriella", 2],
        ["harry potter", "mariana", 31],
        ["diário de um banana", "miguel", 17],
        ["battle royale", "viviane", 5],
        ["a culpa é das estrelas", "laura", 10],
        ["o pequeno príncipe", "davi", 6],
        ["o hobbit", "josé", 12]
    ]

    livrosposetedias = [livro for livro in livros if livro[2] > 7]
    print("livros emprestados há mais de 7 dias:")
    
    for titulo, usuario, dias in livrosposetedias:
        print(f"- {titulo} (nome: {usuario}, dias: {dias})")

    livromaistempo = max(livros, key=lambda x: x[2])
    print(f"\nlivro emprestado há mais tempo: {livromaistempo[0]} (nome: {livromaistempo[1]}, dias: {livromaistempo[2]})")

    usuariospossuilivros = list(set(livro[1] for livro in livros))
    print("\nusuários com livros emprestados:")

    for usuario in usuariospossuilivros:
        print(f"- {usuario}")

    mediadiasemprestimo = sum(livro[2] for livro in livros) / len(livros)
    print(f"\nmédia de dias de empréstimo: {mediadiasemprestimo:.2f} dias")

biblioteca()