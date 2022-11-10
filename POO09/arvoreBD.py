from Pessoa import Pessoa

class ArvoreDB:
    def __init__(self):
        self.pessoaList = []


    def cadPessoa(self, nome, idade, nomePai, nomeMae):
        for pessoa in self.pessoaList:
            if (pessoa.nome == nome and pessoa.idade == idade):
                return "O cadastro informado já existe!"

        self.pessoaList.append(Pessoa(nome, idade, nomePai, nomeMae))
        return "Pessoa cadastrada com Sucesso!"


