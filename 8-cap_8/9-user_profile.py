# ---------------------------------------------------------------------------- #
#               Usando argumentos nomeados arbitrários (**kwargs)              #
# ---------------------------------------------------------------------------- #

def build_profile(first, last, **user_info):
    """ cria um dicionario contendo tudo o que sabemos sobre um usuario"""
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile(
    'albert', 'einstein', location='princeton', field='physics'
)

print(user_profile)