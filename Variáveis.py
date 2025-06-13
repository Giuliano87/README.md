# Variáveis.py

nome = "Fagner Jacob" # Variável global
idade = 37 # Variável global
altura = 1.75 # Variável global
peso = 75 # Variável global
cidade = "São Paulo" # Variável global

# Acessando as variáveis globais
print("Nome:", nome) # Imprime o valor da variável global
print("Idade:", idade) # Imprime o valor da variável global
print("Altura:", altura) # Imprime o valor da variável global   
print("Peso:", peso) # Imprime o valor da variável global
print("Cidade:", cidade) # Imprime o valor da variável global

# Acessando as variáveis locais
def imprimir_dados():   
    local_nome = "Fagner" # Variável local
    local_idade = 37 # Variável local
    print("Nome:", local_nome) # Imprime o valor da variável local
    print("Idade:", local_idade) # Imprime o valor da variável local
    
def imprimir_dados_completo():
    local_nome = "Fagner" # Variável local
    local_idade = 37 # Variável local
    local_altura = 1.75 # Variável local
    local_peso = 75 # Variável local
    local_cidade = "São Paulo" # Variável local
    print("Nome:", local_nome) # Imprime o valor da variável local
    print("Idade:", local_idade) # Imprime o valor da variável local
    print("Altura:", local_altura) # Imprime o valor da variável local
    print("Peso:", local_peso) # Imprime o valor da variável local
    print("Cidade:", local_cidade) # Imprime o valor da variável local