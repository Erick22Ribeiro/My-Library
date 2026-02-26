from django.shortcuts import render, redirect
from core.services.openlibrary import procurar_livros
from core.services.googlebooks import procurar_livros_g
from core.models import Livro

# Create your views here.
def home(request):

    livros = Livro.objects.all()

    livro_quero = Livro.objects.filter(tipo = 'quero')
    livro_comprado = Livro.objects.filter(tipo = 'comprado')
    livro_lido = Livro.objects.filter(tipo = 'lido')

    if request.method == 'POST':

        livro_id = request.POST.get('livro_id')
        novo_tipo = request.POST.get('tipo')

        livro = Livro.objects.get(id = livro_id)

        if novo_tipo == 'remover':

            livro.delete()

        else:

            livro.tipo = novo_tipo

            livro.save()

    context = {
        'livros': livros,
        'livros_quero': livro_quero,
        'livros_comprado': livro_comprado,
        'livros_lido': livro_lido,
    }
    
    return render(request, "core/home.html", context)


def buscar(request):

    query = request.GET.get("q")

    livros = []

    if query:
        #livros = procurar_livros(query)  #API Open Library
        livros = procurar_livros_g(query)  #API Google Books

    if request.method == 'POST':

        #Livro.objects.all().delete()

        Livro.objects.create(
            
            titulo = request.POST['titulo'],
            categoria = request.POST['categoria'],
            autor = request.POST['autor'],
            ano = request.POST['ano'],
            paginas = request.POST['paginas'],
            capa = request.POST['capa'],
            tipo = request.POST['tipo'],

        )

        return redirect('buscar')

    return render(request, "core/buscar.html", {"livros": livros, "query": query})


def livros(request):

    return render(request, "core/livros.html")