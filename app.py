import random # importando a biblioteca random
from datetime import datetime   # importando a biblioteca datetime

class ChatAvancado: # chat avançado
    def __init__(self): # construtor da classe
        self.historico = [] # lista para armazenar o histórico da conversa
        self.saudacoes = ["oi", "olá", "eae", "e aí", "hello", "hi"] # lista de saudações
        self.despedidas = ["tchau", "adeus", "até mais", "flw", "sair"] # lista de despedidas
        self.respostas = { # dicionário de respostas
            "como você está": ["Estou ótimo, obrigado por perguntar!", "Funcionando perfeitamente!", "100% operacional!"],
            "qual seu nome": ["Sou o ChatPython, seu assistente digital.", "Me chamam de BotPython.", "Pode me chamar de CP."],
            "que horas são": [f"Agora são {datetime.now().strftime('%H:%M')}."],
            "hoje é que dia": [f"Hoje é {datetime.now().strftime('%d/%m/%Y')}."]
        }
    def iniciar(self): # método para iniciar o chat
        self._adicionar_ao_historico("Sistema", "Chat iniciado") # adicionando ao histórico
        print("\n" + "="*50) # imprimindo o cabeçalho
        print("CHAT AVANÇADO PYTHON".center(50)) # imprimindo o título
        print("Digite 'ajuda' para ver os comandos disponíveis".center(50)) # imprimindo a ajuda
        print("="*50 + "\n") # imprimindo o rodapé
        
        while True: # loop infinito
            mensagem = input("Você: ").strip().lower() # input da mensagem do usuário
            
            if not mensagem: # se a mensagem estiver vazia, pula para o próximo loop
                continue
                
            self._adicionar_ao_historico("Usuário", mensagem) # adicionando a mensagem ao histórico
            
            if mensagem in self.despedidas: # se a mensagem for uma despedida, responde adequadamente
                self._responder_despedida() # chama o método para responder a despedida
                break
                
            resposta = self._processar_mensagem(mensagem) # chama o método para processar a mensagem
            print(f"ChatBot: {resposta}") # imprime a resposta do chatbot
            self._adicionar_ao_historico("ChatBot", resposta) # adiciona a resposta ao histórico
    
    def _processar_mensagem(self, mensagem): # método para processar a mensagem
        if mensagem == "ajuda": # se a mensagem for "ajuda", mostra a ajuda
            return self._mostrar_ajuda()
        elif mensagem == "historico": # se a mensagem for "historico", mostra o histórico
            return self._mostrar_historico()
        elif any(saudacao in mensagem for saudacao in self.saudacoes): # se a mensagem contiver uma saudação, responde adequadamente
            return random.choice(["Olá! Como posso ajudar?", "Oi! Em que posso ser útil?", "E aí! Qual a boa?"])
        
        for pergunta, respostas in self.respostas.items(): # para cada pergunta e resposta no dicionário
            if pergunta in mensagem: # se a pergunta estiver na mensagem, responde adequadamente
                return random.choice(respostas) # retorna uma resposta aleatória
        
        return random.choice([ # se nenhuma resposta for encontrada, retorna uma mensagem aleatória
            "Não entendi... pode reformular?",
            "Interessante... mas não sei responder isso.",
            "Minhas respostas são limitadas, tente outra pergunta.",
            "Você poderia perguntar de outra forma?"
        ])  
        if mensagem in self.despedidas: # se a mensagem for uma despedida, responde adequadamente
                self._responder_despedida() # chama o método para responder a despedida
                break
        resposta = self._processar_mensagem(mensagem) # chama o método para processar a mensagem
        print(f"ChatBot: {resposta}") # imprime a resposta do chatbot
        self._adicionar_ao_historico("ChatBot", resposta) # adiciona a resposta ao histórico
    
    def _responder_despedida(self): # método para responder a despedida
        despedida = random.choice([ # escolhe uma resposta aleatória para a despedida
            "Até logo! Volte quando quiser.",
            "Foi um prazer conversar!",
            "Encerrando o chat. Tenha um ótimo dia!"
        ])
        print(f"ChatBot: {despedida}") # imprime a resposta do chatbot
        self._adicionar_ao_historico("Sistema", "Chat encerrado") # adiciona a mensagem ao histórico
    
    def _mostrar_ajuda(self): # método para mostrar a ajuda
        return ("Comandos disponíveis:\n"
                "- 'historico': Mostra todo o histórico da conversa\n"
                "- 'sair': Encerra o chat\n"
                "- 'ajuda': Mostra esta mensagem\n"
                "Você também pode perguntar sobre:\n"
                "- Como você está?\n"
                "- Qual seu nome?\n"
                "- Que horas são?\n"
                "- Hoje é que dia?")
    
    def _mostrar_historico(self): # método para mostrar o histórico
        if not self.historico: # se o histórico estiver vazio, retorna uma mensagem
            return "O histórico está vazio."
        
        historico_formatado = "\n".join( # formata o histórico em uma string
            f"[{hora}] {remetente}: {mensagem}"
            for remetente, mensagem, hora in self.historico
        )
        return f"Histórico da conversa:\n{historico_formatado}"
    def processar_mensagem(self, mensagem): # método para processar a mensagem
        if mensagem == "ajuda": # se a mensagem for "ajuda", mostra a ajuda
            return self._mostrar_ajuda() # chama o método para mostrar a ajuda

        elif mensagem == "historico": # se a mensagem for "historico", mostra o histórico
            return self._mostrar_historico() # chama o método para mostrar o histórico
        elif any(saudacao in mensagem for saudacao in self.saudacoes): # se a mensagem contiver uma saudação, responde adequadamente
            return random.choice(["Olá! Como posso ajudar?", "Oi! Em que posso ser útil?", "E aí! Qual a boa?"])
        for pergunta, respostas in self.respostas.items(): # para cada pergunta e resposta no dicionário
            if pergunta in mensagem: # se a pergunta estiver na mensagem, responde adequadamente
                return random.choice(respostas) # retorna uma resposta aleatória
        return random.choice ([ # se nenhuma resposta for encontrada, retorna uma mensagem aleatória    
            "Interessante... mas não sei responder isso.",
            "Minhas respostas são limitadas, tente outra pergunta.",
            "Você poderia perguntar de outra forma?"        
        ])
        "Interessante... mas não sei responder isso.",  
        for pergunta, respostas in self.respostas.items(): # para cada pergunta e resposta no dicionário
            if pergunta in mensagem: # se a pergunta estiver na mensagem, responde adequadamente
                return random.choice(respostas) # retorna uma resposta aleatória        
        return random.choices # se nenhuma resposta for encontrada, retorna uma mensagem aleatória            
        return random.choice(respostas) # retorna uma resposta aleatória  
              
        
        return random.choice([ # se nenhuma resposta for encontrada, retorna uma mensagem aleatória
            "Não entendi... pode reformular?",
            "Interessante... mas não sei responder isso.",
            "Minhas respostas são limitadas, tente outra pergunta.",
            "Você poderia perguntar de outra forma?"
        ])
    
    def _adicionar_ao_historico(self, remetente, mensagem): # método para adicionar a mensagem ao histórico
        hora_atual = datetime.now().strftime("%H:%M:%S") # pega a hora atual
        self.historico.append((remetente, mensagem, hora_atual)) # adiciona a mensagem ao histórico 
    
    def responder_despedida(self): # método para responder a despedida     
        despedida = random.choice([ # escolhe uma resposta aleatória para a despedida
            "Até logo! Volte quando quiser.",
            "Foi um prazer conversar!",
            "Encerrando o chat. Tenha um ótimo dia!"
        ])
        print(f"ChatBot: {despedida}") # imprime a resposta do chatbot
        self._adicionar_ao_historico("Sistema", "Chat encerrado") # adiciona a mensagem ao histórico
    
    def mostrar_ajuda(self): # método para mostrar a ajuda
        return ("Comandos disponíveis:\n"
                "- 'historico': Mostra todo o histórico da conversa\n"
                "- 'sair': Encerra o chat\n"
                "- 'ajuda': Mostra esta mensagem\n"
                "Você também pode perguntar sobre:\n"
                "- Como você está?\n"
                "- Qual seu nome?\n"
                "- Que horas são?\n"
                "- Hoje é que dia?")
    
    def mostrar_historico(self): # método para mostrar o histórico  
        if not self.historico: # se o histórico estiver vazio, retorna uma mensagem
            return "O histórico está vazio."
        historico_formatado = "\n".join( # formata o histórico em uma string

            f"[{hora}] {remetente}: {mensagem}" # formata a mensagem do histórico
            for remetente, mensagem, hora in self.historico
        )
    def adicionar_ao_historico(self, remetente, mensagem): # método para adicionar a mensagem ao histórico

        hora_atual = datetime.now().strftime("%H:%M:%S") # pega a hora atual
        self.historico.append((remetente, mensagem, hora_atual)) # adiciona a mensagem ao histórico 
        return self.historico   # retorna o histórico
        hora_atual = datetime.now().strftime("%H:%M:%S") # pega a hora atual
        self.historico.append((remetente, mensagem, hora_atual)) # adiciona a mensagem ao histórico     
        return self.historico   # retorna o histórico
        self.historico.append((remetente, mensagem, hora_atual)) # adiciona a mensagem ao histórico     

if __name__ == "__main__": # se o arquivo for executado diretamente, executa o código abaixo
    chat = ChatAvancado() # instancia o chat
    chat.iniciar() # inicia o chat



