class ContaBacaria:
    def __init__(self, titular, numero_conta, saldo, vip):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.vip = vip

    def sacar(self, valor):
        if valor > self.saldo:
            print("SALDO INSUFICIENTE!")
        else:
            self.saldo -= valor

            return valor

    def depositar(self, valor):
        if valor < 0:
            print("VALOR A SER DEPOSITADO INFERIOR A 0!")
        else:
            self.saldo += valor

    def mostrar(self):
        print(self.titular)
        print(self.numero_conta)
        print(self.saldo)
        print(self.vip)

conta1 = ContaBacaria("John Doe", 132, 400, False)

conta1.depositar(200)

conta1.sacar(600)

conta1.mostrar()