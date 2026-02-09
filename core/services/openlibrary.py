import requests

def procurar_livros(query):

    url = 'https://openlibrary.org/search.json'
    response = requests.get(url, params = {'q':query}, timeout = 5)
    dados = response.json()

    livros = []

    for item in dados['docs'][:10]:

        livros.append({
            "title": item.get("title"),
            "author": item.get("author_name", ["Autor desconhecido"])[0],
            "year": item.get("first_publish_year"),
            "isbn": item.get("isbn", [None])[0],
        })

    return livros