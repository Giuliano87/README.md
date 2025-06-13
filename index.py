class Conta:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")

    def deposito(self, valor):
        self.saldo += valor
        print("Deposito realizado com sucesso!")

    def transferencia(self, valor, conta_destino):
        if self.saldo >= valor:
            self.saque(valor)
            conta_destino.deposito(valor)
        else:
            print("Saldo insuficiente para transferência!")

