# ---------------------------------------------------------------------------- #
#!                           8.10 Enviando mensagens                           #
# ---------------------------------------------------------------------------- #

# Comece com uma cópia do seu programa do Exercício 8.9. 

# Escreva uma função chamada send_messages() para exibir cada mensagem de texto e passe cada mensagem para uma nova lista chamada sent_messages à medida que é exibida. 

# Após chamar a função, exiba ambas as listas para ter certeza de que as mensagens foram corretamente transferidas.


mensagens = [
    "Olá, tudo bem?",
    "Bom dia!",
    "Como vai você?",
    "Até mais tarde!",
    "Obrigado!",
    "Por favor...",
    "Parabéns!",
    "Feliz aniversário!",
    "Boa sorte!",
    "Até logo!",
    "Que horas são?",
    "Preciso de ajuda.",
    "Estou chegando.",
    "Te amo!",
    "Boa noite!",
    "Com licença.",
    "Desculpe.",
    "Parabéns pelo trabalho!",
    "Fique bem!",
    "Nos vemos amanhã."
]

sent_messages = []

def send_messages(message_list):
    """Exibe cada mensagem e a move para sent_messages."""
    while message_list:
        current_message = message_list.pop()
        print(current_message)
        sent_messages.append(current_message)

    print(f"Lista 1 :\n{mensagens}")
    print(f"Lista 2 :\n {sent_messages}")


send_messages(mensagens)