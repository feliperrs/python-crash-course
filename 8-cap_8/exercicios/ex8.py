# ---------------------------------------------------------------------------- #
#!                           8.8 Álbums de usuários                            #
# ---------------------------------------------------------------------------- #

# Comece com seu programa do Exercício 8.7. 

# Escreva um loop while que possibilite aos usuários inserir o artista e o título de um álbum. 

# Após receber essas informações, chame make_album() com a entrada do usuário e exiba o dicionário criado. 

# Não se esqueça de incluir um valor de saída no loop while.

def make_album(artist_name, album_name, song_number=None):
    """Retorna um dicionario com informações sobre um album de musicas"""
    album = {'artist_name' : artist_name, 'album_name' : album_name}
    if song_number:
        album['song_number'] = song_number 

    return print(album)

while True:
    print("Insira o nome do artista")
    artista = input(">> ")
    print("Insira o nome do album")
    album = input(">> ")
    print("Deseja incluir o numero de músicas do album?(s/n)")
    decisao = input(">> ").lower()
    if decisao == 's':
        print("Qual o número de musicas?")
        n_musicas = input(">> ")
        make_album(artista, album, n_musicas)
    else:
        make_album(artista, album)
    
    print("\nDeseja adicionar mais musicas?(s/n)")
    escolha = input(">> ").lower()
    if escolha == 's':
        continue
    else:
        break
