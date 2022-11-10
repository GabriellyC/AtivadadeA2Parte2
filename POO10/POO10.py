#Escreva um programa em Python para gerenciar uma Instituição Financeira. Para tanto, iniciar criando uma classe chamada ContaBancaria para
#representar uma conta bancária. Esta classe deverá conter:

from ContaBancaria import ContaBancaria

conta = ContaBancaria()


menu = 1
while (menu !=5):
  print("1 - Saldo.")
  print("2 - Depositar.")
  print("3 - Sacar.")
  print("4 - Data de Abertura.")
  print("5 - Sair.")

  menu = int(input("Digite a opção: "))

  if menu == 1:
    print(f"O valor do salto é: {conta.saldoAtual()}")
    print(f"O valor do salto formatado é: {conta.saldoFormatado()}")

  elif menu == 2:
    valorDepositar = float(input("Digite o valor que deseja depositar: "))
    print(conta.depositar(valorDepositar))

  elif menu == 3:
    sacarValor = float(input("Digite o valor que deseja sacar: "))
    print(conta.sacar(sacarValor))

  elif menu == 4:
    print(f"A data de abertura é: {conta.dataAbertura()}")
    print(f"A data de abertura formatada é: {conta.dataFormatada()}")

  elif menu == 5:
    break
  else:
    print("Digite uma opção válida!")