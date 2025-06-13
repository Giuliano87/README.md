# Lista para armazenar as transações
transacoes = []

# Função para adicionar uma transação
def registrar_transacao(valor):
    if isinstance(valor, (int, float)):
        transacoes.append(valor)
        print(f"Transação registrada: {'Depósito' if valor > 0 else 'Saque'} de R${abs(valor):.2f}")
    else:
        print("Erro: o valor da transação deve ser numérico.")

# Função para calcular o saldo final
def calcular_saldo():
    return sum(transacoes)

# Exemplo de uso
registrar_transacao(1000.00)  # depósito
registrar_transacao(-200.00)  # saque
registrar_transacao(500.00)   # depósito
registrar_transacao(-100.00)  # saque

# Exibe as transações e o saldo final
print("\nTransações realizadas:")
for i, t in enumerate(transacoes, start=1):
    tipo = "Depósito" if t > 0 else "Saque"
    print(f"{i}. {tipo}: R${abs(t):.2f}")

print(f"\nSaldo final: R${calcular_saldo():.2f}")
    
    