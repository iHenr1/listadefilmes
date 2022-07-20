import requests
import json

def requisicao (titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=bb12ae3f&t=' + titulo)
        dicionario = json.loads(req.text)
        return dicionario
    except Exception as e:
        print('Erro na requisição:', e)
        return None

def printar_detalhes(x):
    print('Título:', x['Title'])
    print('Atores:', x['Actors'])
    print('Anos:', x['Year'])
    print('Diretor:', x['Director'])
    print('Notas:', x['imdbRating'])
    print('Premios:', x['Awards'])
    print('Sinopse:', x['Plot'])
    print('Poster:', x['Poster'])

    print('')

sair = False
while not sair:
    op = input('Escreva o nome do filme ou SAIR para fechar o programa: ')

    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado')
        else:
            printar_detalhes(filme)
