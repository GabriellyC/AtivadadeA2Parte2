from Livro import livro
from Pessoa import pessoa
from Emprestimo import emprestimo

class livrosDB:
    listPessoa = []
    listEmprestimo = []

    estoqueLivro = []
    def gerarBD(self):
        self.estoqueLivro.append(livro(1, "O cavaleiro das sombras", "João Pessoa", "Fantasia", 2003, 3))
        self.estoqueLivro.append(livro(2, "O feiticeiro da rua 13", "Margaret lentgh", "Fantasia", 2002, 4))
        self.estoqueLivro.append(livro(3, "Gatos e Sapatos", "Carol Ricci", "Comédia", 1999, 5))
        self.estoqueLivro.append(livro(4, "Nas ruas de Nova York", "Edith lovelance", "Romance", 2018, 6))
        self.estoqueLivro.append(livro(5, "Entre os becos de berlim", "Karol Trindade", "Romance", 2000, 4))
        self.estoqueLivro.append(livro(6, "A biologia a seu favor", "Frederico Josen", "Didático", 2005, 6))
        self.estoqueLivro.append(livro(7, "O anel perdido", "Fernando Torres", "Fantasia", 2007, 6))
        self.estoqueLivro.append(livro(8, "O mistério da casa 420", "Marta Carneiro", "Suspense", 2015, 3))
        self.estoqueLivro.append(livro(9, "O caso 137", "Jack Devon", "Terror", 2004, 6))
        self.estoqueLivro.append(livro(10, "O lobo na minha rua", "Priscila Fernandes", "Terror", 2016, 4))
        self.estoqueLivro.append(livro(11, "A pedra no meu sapato", "Carol Ricci", "Comédia", 2000, 3))
        self.estoqueLivro.append(livro(12, "Debaixo da egua", "Jose Capitol", "Comédia", 2003, 3))
        self.estoqueLivro.append(livro(13, "Filosofia, o inicio", "Frank Bill", "Didático", 1999, 2))
        self.estoqueLivro.append(livro(14, "A volta dos tempos", "Melisa Melber", "Fantasia", 2005, 1))


    def realizarEmp(self, nome, telefone, livro, dataEmprest, dataDevol):
        for item in self.estoqueLivro:
            if(item.codigo == livro):
                self.listPessoa.append(pessoa(nome, telefone))
                self.listEmprestimo.append(emprestimo(livro, nome, dataEmprest, dataDevol))
                print("Empréstimo realizado com sucesso!")
                return
        print("Código não encontrado!")


    def devolucao (self, nome, codLivro):
        if len(self.listEmprestimo) != 0:
            cont = 0
            for item in self.listEmprestimo:
                if item.codLivro == codLivro and item.nomePessoa == nome:
                    self.listEmprestimo.pop(cont)
                    return "Devolução feita com sucesso!".format(nome)
                else:
                    return "Empréstimo não encontrado!"

    def verificarEstoque(self, codigo):
        for item in self.estoqueLivro:
            if(item.codigo == codigo and item.qtd >= 1):
                return True

        return False



    def retirarEstoque(self, codigo):
        for item in self.estoqueLivro:
            if (item.codigo == codigo):
                item.qtd = item.qtd - 1

    def devolverEstoque(self, codigo):
        for item in self.estoqueLivro:
            if (item.codigo == codigo):
                item.qtd = item.qtd + 1