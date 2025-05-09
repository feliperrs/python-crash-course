# ---------------------------------------------------------------------------- #
#!                                  8.7 Álbum                                  #
# ---------------------------------------------------------------------------- #

# Escreva uma função chamada make_album() que crie um dicionário representando um álbum de música. 

# A função deve ter o nome de um artista e o título do álbum, e deve retornar um dicionário com essas duas informações. 

# Utilize a função para criar três dicionários representando álbuns distintos.

# Exiba cada valor de retorno para mostrar que os dicionários estão armazenando adequadamente as informações do álbum.

# Use None para adicionar um parâmetro opcional ao make_album() que possibilite armazenar o número de músicas em um álbum. 

# Se a linha chamadora incluir esse valor para o número de músicas, adicione esse valor ao dicionário do álbum. 

# Crie, pelo menos, uma nova chamada de função que inclua o número de músicas em um álbum.

def make_album(artist_name, album_name, song_number=None):
    """Retorna um dicionario com informações sobre um album de musicas"""
    album = {'artist_name' : artist_name, 'album_name' : album_name}
    if song_number:
        album['song_number'] = song_number 

    return print(album)

make_album('michael jackson', 'thriller', )
make_album('the beatles', 'abbey road', )
make_album('prince', 'purple rain', )
make_album('frank ocean' 'blonde', 17)