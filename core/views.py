from django.shortcuts import render
from core.services.openlibrary import procurar_livros

# Create your views here.
def home(request):

    query = request.GET.get("q")
    livros = []

    if query:
        livros = procurar_livros(query)

    return render(request, "core/home.html", {"livros": livros, "query": query})