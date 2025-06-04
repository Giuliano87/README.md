class conta_bancaria:

    def __init__(self, numero, titular, saldo):
        self.numero = numero    
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor  # Corrected the variable name to 'valor' to match the parameter

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor  # Corrected the variable name to 'valor' to match the parameter
            return True
        
        else:
            return False
        def extrato(self):
            print("Saldo: ", self.saldo)
            
        def transferir(self, valor, destino):
            if self.sacar(valor):
                destino.depositar(valor)
                print("Transferência realizada com sucesso!")
                
            else:
                print("Saldo insuficiente para transferência.")
                
                # Creating objects of the class conta_bancaria
                
conta1 = conta_bancaria(1234, "John Doe", 5000)
conta2 = conta_bancaria(5678, "Jane Doe", 10000)

# Testing the methods of the class conta_bancaria       
















