def sacar(cliente, valor):
    if not (cliente['saldo'] - valor < 0):
        cliente['saldo'] -= valor

        print(valor)
    else:
        print('SALDO INSUFICIENTE!')

def depositar(cliente, valor):
    cliente['saldo'] += valor

    print("VALOR DEPOSITADO COM SUCESSO!")

def mostrar_extrato(cliente):
    print(f"SEU SALDO É {cliente['saldo']}")
