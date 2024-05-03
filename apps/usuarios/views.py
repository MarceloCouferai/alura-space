from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome=form['nome_login'].value() #recebe dados
            senha=form['senha'].value()

        usuario = auth.authenticate(request, username = nome, password=senha) #autentica se existe na base de dados com biblioteca auth
 
        if usuario is not None:
            auth.login(request, usuario)
            return redirect('index')

        else:
            messages.error(request, 'Erro ao efetual o login, verifique dos dados novamente')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})



def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST': #pega informações e colocar dentro de outro formulário
        form = CadastroForms(request.POST) # puxa formulário
        
        if form.is_valid(): # <- verifica se o formulário está válido
            
            nome = form['nome_cadastro'].value() #pegando informações escritas no formulário
            email = form['email'].value()
            senha = form['senha'].value()
            confirmar_senha = form['confirmar_senha'].value()

            if User.objects.filter(username=nome).exists(): #verificando se o usuário já existe na base de dados
                messages.error(request, 'Esse usuário já existe!')
                return redirect('cadastro')
            
            usuario = User.objects.create_user( #criando usuário na base de dados e apontando cada item para a base (nome, email e senha)
                username = nome,
                email = email,
                password = senha
            )
            usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})



def logout(request):
    auth.logout(request)
    messages.success(request, 'Você saiu.')
    return redirect('login')