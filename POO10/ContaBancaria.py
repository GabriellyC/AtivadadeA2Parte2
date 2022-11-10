import datetime as date

class ContaBancaria:
    def __init__(self):
        self.__saldo = float(0.0)
        self.__dataAbertura = date.datetime.now()

    def saldoAtual(self):
        return self.__saldo

    def saldoFormatado(self):
        return f"R$ {self.__saldo:,.2f}".replace('.','v').replace(',','.').replace('v',',')

    def dataAbertura(self):
        return self.__dataAbertura

    def dataFormatada(self):
        return self.__dataAbertura.strftime("%d/%m/%y")

    def depositar(self, valorDeposito):
        if(valorDeposito > 0):
            self.__saldo = self.__saldo +valorDeposito
            return f"Valor de R${valorDeposito:.2f} foi depositado com sucesso."

        return f"Erro ao tentar realizar o deposito."

    def sacar(self, valorSaque):
        if (valorSaque > 0):
            if((self.__saldo - valorSaque) >= 0):
                self.__saldo = self.__saldo - valorSaque
                return f"Saque de R${valorSaque:.2f} foi efetuado com sucesso!"

        return f"Erro ao tentar realizar saque."