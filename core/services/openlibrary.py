import requests

def procurar_livros(query):

    url = 'https://openlibrary.org/search.json'
    response = requests.get(url, params = {'q':query}, timeout = 5)
    dados = response.json()

    livros = []

    for item in dados['docs']:

        capa_id = item.get('cover_i')

        if capa_id:
            capa_url = f'https://covers.openlibrary.org/b/id/{capa_id}-M.jpg'

        else:
            capa_id = None

        livros.append({
            "title": item.get("title"),
            "author": item.get("author_name", ["Autor desconhecido"])[0],
            "year": item.get("first_publish_year"),
            "isbn": item.get("isbn", [None])[0],
            'capa': capa_url,
        })

    return livros