import os

# vetores
saques = []
depositos = []

# armazena valores para o histórico
def guarda_saque(valor):
    saques.append(valor)

def guarda_deposito(valor):
    depositos.append(valor)

# função para realizar o saque
def sacar(saldo):
    try:
        saque = float(input("Valor do saque: R$ "))
    except ValueError:
        print("Entrada inválida!\n")
        return saldo

    if saque > saldo:
        print("Não há como fazer esse saque!\n")
        return saldo

    total = saldo - saque
    guarda_saque(saque)

    print("\nDinheiro:\n")

    # cálculo para notas e moedas
    notas = [100, 50, 20, 10, 5, 2, 1]
    moedas = [0.5, 0.25, 0.1, 0.05]

    for nota in notas:
        qtd = int(saque // nota)
        if qtd > 0:
            print(f"Notas/Moedas de {nota}: {qtd}")
            saque -= qtd * nota

    for moeda in moedas:
        qtd = int(saque // moeda)
        if qtd > 0:
            print(f"Moedas de {moeda:.2f}: {qtd}")
            saque -= qtd * moeda

    print("\nSaque realizado com sucesso!\n")
    return total

# função para realizar o depósito
def depositar(saldo):
    try:
        valor = float(input("Valor do depósito: R$ "))
    except ValueError:
        print("Entrada inválida!\n")
        return saldo

    saldo += valor
    guarda_deposito(valor)
    print("\nDepósito concluído com sucesso!\n")
    return saldo

# função para mostrar o histórico
def historico():
    if saques:
        print("Saques:\n")
        for saque in reversed(saques):
            print(f"Sacou: R${saque:.2f}")

    if depositos:
        print("\nDepósitos:\n")
        for deposito in reversed(depositos):
            print(f"Depositou: R${deposito:.2f}")

# função para mostrar o extrato
def extrato(saldo):
    print(f"Total - R${saldo:.2f}\n")
    print("EXTRATO\n")

    if not saques and not depositos:
        print("Não houve nenhuma transação!\n")
    else:
        historico()
    print()

# função principal
def main():
    saldo = 100.00
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("BANCO ELETRÔNICO!\n")
        print(f"Total: R${saldo:.2f}\n")
        print("1- Sacar \n2- Depositar \n3- Extrato \n4- Sair\n")
        
        opcao = input("Opção: ")

        if opcao == "1":
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Total: R${saldo:.2f}\n")
            saldo = sacar(saldo)
            input("Pressione ENTER para continuar...")
        elif opcao == "2":
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Total: R${saldo:.2f}\n")
            saldo = depositar(saldo)
            input("Pressione ENTER para continuar...")
        elif opcao == "3":
            os.system("cls" if os.name == "nt" else "clear")
            extrato(saldo)
            input("Pressione ENTER para continuar...")
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Digite outra opção!")
            input("Pressione ENTER para continuar...")

if __name__ == "__main__":
    main()
