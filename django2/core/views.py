from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm, ProdutoModelForm

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Mensagem enviada com sucesso')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar mensagem')

    context = {
        'form': form
    }

    return render(request, 'contato.html', context)

def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            form = ProdutoModelForm()
            messages.success(request, 'Produto salvo com sucesso')
        else:
            messages.error(request, 'Erro ao salvar o produto')

    context = {
        'form': form
    }

    return render(request, 'produto.html', context)