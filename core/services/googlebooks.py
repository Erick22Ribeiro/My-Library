import requests
import json

def procurar_livros_g(query):

    url = 'https://www.googleapis.com/books/v1/volumes'

    params = {
        'q': query,
    }

    response = requests.get(url, params = params, timeout=5)

    dados = response.json()

    livros = []

    for item in dados.get('items', []):

        info = item.get('volumeInfo', {})

        livros.append({
            'titulo': info.get('title'),
            'autor': info.get('authors', ['Autor desconhecido'])[0],
            'ano': info.get('publishedDate'),
            'capa': info.get('imageLinks', {}).get('thumbnail'),
            'categoria': info.get('categories', ['Categoria desconhecida'])[0],
        })

    return livros