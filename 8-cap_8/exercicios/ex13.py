# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #

# Comece com uma cópia do user_profile.py da página 196. 

# Crie um perfil de si mesmo chamando build_profile(), com seu primeiro nome e sobrenome e três outros pares chave-valor que o representem.

def build_profile(first, last, **user_info):
    """ cria um dicionario contendo tudo o que sabemos sobre um usuario"""
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile(
    'felipe', 
    'santos', 
    location='sao paulo', 
    field='computer science', 
    working= False
)

print(user_profile)