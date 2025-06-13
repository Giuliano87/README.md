# Lista para armazenar as transações
from index import Conta 
transacoes = [] # Lista para armazenar as transações
nome = input("Digite seu nome:")  # Pede o nome do usuário
cpf = input("Digite seu CPF:") # Pede o CPF do usuário
agencia = input("Digite sua agência:") # Pede a agência do usuário    
conta = input("Digite sua conta:") # Pede a conta do usuário
banco = input("Digite o nome do banco:") # Pede o nome do banco

# Cria uma instância da classe Conta
print(f"Seu CPF é {cpf}, sua agência é {agencia} e sua conta é {conta}.") # Exibe os dados do usuário
print(f"Você está utilizando o banco {banco}.") # Exibe o nome do banco

# Exibe os dados do usuário
print(f"Olá, {nome}! Seja bem-vindo(a) à sua conta bancária.") # Exibe o nome do usuário
print(f"Seu CPF é {cpf}, sua agência é {agencia} e sua conta é {conta}.") # Exibe os dados do usuário


# Função para adicionar uma transação
def registrar_transacao(valor): # Função para adicionar uma transação
    if isinstance(valor, (int, float)): # Verifica se o valor é numérico
        transacoes.append(valor) # Adiciona a transação na lista
        print(f"Transação registrada: {'Depósito' if valor > 0 else 'Saque'} de R${abs(valor):.2f}") # Exibe a transação registrada 
        print("Erro: o valor da transação deve ser numérico.") # Exibe a mensagem de erro.

# Função para calcular o saldo final
def calcular_saldo(): # Função para calcular o saldo final
    return sum(transacoes) # Retorna a soma das transações.

# Exemplo de uso
registrar_transacao(1000.00)  # depósito
registrar_transacao(-200.00)  # saque
registrar_transacao(500.00)   # depósito
registrar_transacao(-100.00)  # saque

# Exibe as transações e o saldo final
print("\nTransações realizadas:") # Exibe a mensagem de transações realizadas
for i, t in enumerate(transacoes, start=1): # Exibe as transações
    tipo = "Depósito" if t > 0 else "Saque" # Verifica se é um depósito ou um saque
    print(f"{i}. {tipo}: R${abs(t):.2f}") # Exibe a transação
    print(f"\nSaldo final: R${calcular_saldo():.2f}") # Exibe o saldo final
    
    