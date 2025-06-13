def registrar_transacoes():
    print("Bem-vindo ao Sistema de Registro de Transações Bancárias")
    print("Digite as transações (depósitos como valores positivos, saques como negativos)")
    print("Digite 'fim' para terminar e calcular o saldo\n")
    
    transacoes = []
    
    while True:
        entrada = input("Digite o valor da transação (ex: 100 ou -50): ")
        
        if entrada.lower() == 'fim':
            break
            
        try:
            valor = float(entrada)
            transacoes.append(valor)
            print(f"Transação registrada: {valor:.2f}")
        except ValueError:
            print("Valor inválido. Digite um número ou 'fim' para terminar.")
    
    # Calculando o saldo final
    saldo = sum(transacoes)
    
    # Exibindo o relatório
    print("\n===== Relatório de Transações =====")
    for i, transacao in enumerate(transacoes, 1):
        tipo = "Depósito" if transacao >= 0 else "Saque"
        print(f"{i}. {tipo}: R$ {abs(transacao):.2f}")
    
    print("\n===== Saldo Final =====")
    print(f"Total de transações: {len(transacoes)}") # len retorna o número de elementos em uma lista
    print(f"Saldo final da conta: R$ {saldo:.2f}")
    
    if saldo >= 0:
        print("Situação: Saldo positivo")
    else:
        print("Situação: SALDO NEGATIVO - ATENÇÃO")

# Executar o programa
if __name__ == "__main__":
    registrar_transacoes()
    
    