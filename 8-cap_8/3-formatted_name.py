# ---------------------------------------------------------------------------- #
#!                         Retornando um valor simples                         #
# ---------------------------------------------------------------------------- #

def get_formatted_name(first_name, last_name):
    """Retorna um dicionario de informações sobre uma pessoa"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# ---------------------------------------------------------------------------- #
#!                    Definindo um argumento como opcional                     #
# ---------------------------------------------------------------------------- #

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)