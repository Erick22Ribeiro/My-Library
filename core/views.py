from django.shortcuts import render
from core.services.openlibrary import procurar_livros
from core.services.googlebooks import procurar_livros_g

# Create your views here.
def home(request):

    query = request.GET.get("q")

    livros = []

    if query:
        #livros = procurar_livros(query)  #API Open Library
        livros = procurar_livros_g(query)  #API Google Books

    return render(request, "core/home.html", {"livros": livros, "query": query})


def livros(request):

    query = request.GET.get("q")

    livros = []

    if query:
        #livros = procurar_livros(query)  #API Open Library
        livros = procurar_livros_g(query)  #API Google Books

    return render(request, "core/livros.html", {"livros": livros, "query": query})
