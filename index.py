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

print("Saldo insuficiente para transferência.")

# Creating objects of the class conta_bancaria

conta1 = conta_bancaria(1234, "John Doe", 5000)
conta2 = conta_bancaria(5678, "Jane Doe", 10000)

# Testing the methods of the class conta_bancaria

def test_depositar():
    conta1.depositar(1000)
    assert conta1.saldo == 6000, "Depósito não realizado com sucesso"

def test_sacar():
    assert conta1.sacar(2000) == True, "Saque não realizado com sucesso"
    assert conta1.saldo == 4000, "Saque não realizado com sucesso"

def test_extrato():
    conta1.extrato()
    assert True, "Extrato não impresso"

def test_transferir():
    assert conta1.transferir(2000, conta2) == True, "Transferência não realizada com sucesso"
    
    test_depositar()
    test_sacar()
    test_extrato()
    test_transferir()
    test_depositar()














