import modulo_banco as banco

cliente = {
    'saldo': 0
}

banco.depositar(cliente, 200)
banco.sacar(cliente, 100)
banco.sacar(cliente, 200)
banco.mostrar_extrato(cliente)
