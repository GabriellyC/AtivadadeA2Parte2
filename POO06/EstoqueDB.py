from produto import produto


class EstoqueDB:

    estoqueProd = []
    def gerarEstoque(self):
        self.estoqueProd.append(produto(1, "Bandeja de uva", 8.50, 9))
        self.estoqueProd.append(produto(2, "Macarrão", 6.20, 11))
        self.estoqueProd.append(produto(3, "Bandeja de morango", 9.99, 15))
        self.estoqueProd.append(produto(4, "Arroz 5k", 19.90, 15))
        self.estoqueProd.append(produto(5, "Arroz 1kg", 5.50, 14))
        self.estoqueProd.append(produto(6, "Feijao 1kg", 4.50, 11))
        self.estoqueProd.append(produto(7, "Arroz integral 1kg", 6.50, 12))
        self.estoqueProd.append(produto(8, "Melão", 4.99, 10))
        self.estoqueProd.append(produto(9, "Papel higiênico Neve 12 rolos", 7.50, 11))
        self.estoqueProd.append(produto(10, "Shampoo Darling", 7, 8))
        self.estoqueProd.append(produto(11, "Sabonete em barra", 0.99, 13))
        self.estoqueProd.append(produto(12, "Sabonete Liquido 500ml", 9.90, 16))
        self.estoqueProd.append(produto(13, "Condicionador", 10.99, 12))
        self.estoqueProd.append(produto(14, "Creme Dental", 1.99, 16))
        self.estoqueProd.append(produto(15, "Linguiça 1kg", 15.99, 15))
        self.estoqueProd.append(produto(16, "Carne Bovina 1kg", 19.99, 16))
        self.estoqueProd.append(produto(17, "Carne Suína", 18.99, 16))
        self.estoqueProd.append(produto(18, "Miojo turma da mônica", 1.99, 15))


    def verificarEstoque(self, codigo, quantidade):
        for item in self.estoqueProd:
            if(item.codigo == codigo and item.quantidade >= quantidade):
                return True

        return False

    def retirarEstoque(self, codigo, quantidade):
        for item in self.estoqueProd:
            if (item.codigo == codigo):
                item.quantidade = item.quantidade - quantidade







