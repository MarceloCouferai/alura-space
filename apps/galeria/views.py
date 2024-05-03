from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages
from apps.galeria.forms import FotografiaForms


def index(request):
    if not request.user.is_authenticated: #validar se usuario está logado para acessar a index
        messages.error(request, 'Usuário não está logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request,'galeria/index.html', {"cards": fotografias})

    
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html',{"fotografia": fotografia})


def buscar(request):
    if not request.user.is_authenticated: #validar se usuario está logado para acessar a index
        messages.error(request, 'Usuário não está logado')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if 'buscar' in request.GET:  #ter campo escrito na base
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_buscar) #ver se tem dentro do nome o nome buscado(nome_buscar)
    return render(request, 'galeria/index.html', {'cards': fotografias})


def nova_imagem(request):
    if not request.user.is_authenticated: #validar se usuario está logado para acessar a index
        messages.error(request, 'Usuário não está logado')
        return redirect('login')
    
    form = FotografiaForms

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES) #Pega as informações do formulário e coloca na variavel, e pega arquivos do formulário
        if form.is_valid():
            form.save()
            messages.success(request, 'Sua imagem foi adicionada!')
            return redirect('index')

    return render(request,'galeria/nova_imagem.html', {'form': form})


def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id) #pegando fotografia pelo request da fotografia selecionada
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sua imagem foi editada!')

    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Imagem apagada.')
    return redirect('index')


def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)
    return render(request, 'galeria/index.html', {'cards': fotografias})

