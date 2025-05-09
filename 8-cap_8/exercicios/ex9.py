# ---------------------------------------------------------------------------- #
#!                                8.9 Mensagens                                #
# ---------------------------------------------------------------------------- #

# Crie uma lista com uma série de mensagens curtas de texto.

# Passe a lista para uma função chamada show_messages(), que exiba cada mensagem de texto.

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

def show_messages(message_list):
    """Exibe cada mensagem de uma lista de mensagens."""
    for message in message_list:
        print(message)


show_messages(mensagens)