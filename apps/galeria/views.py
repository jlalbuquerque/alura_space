from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib.auth.decorators import login_required
from apps.galeria.forms import FotografiaForms
from django.contrib import messages


@login_required(login_url='login')
def index(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})


@login_required(login_url='login')
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})


@login_required(login_url='login')
def buscar(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    if "categoria" in request.GET:
        categoria = request.GET['categoria']
        if categoria:
            fotografias = fotografias.filter(categoria__icontains=categoria)

    return render(request, "galeria/buscar.html", {"cards": fotografias})

@login_required(login_url='login')
def nova_imagem(request):
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.instance.publicada = True
            form.save()
            messages.success(request, "Nova fotografia cadastrada!")
            return redirect('index')
    form = FotografiaForms()
    context = {'form': form}
    return render(request, 'galeria/nova_imagem.html', context)


@login_required(login_url='login')
def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)
    
    context = {'form': form, 'foto_id': foto_id}
    
    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem editada com sucesso!')
            return redirect('index')
    
    return render(request, 'galeria/editar_imagem.html', context=context)


@login_required(login_url='login')
def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Fotografia deletada com sucesso')
    return redirect('index')

@login_required(login_url='login')
def filtro(request, categoria):
    if categoria == 'TODOS':
        return redirect('index')
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True, categoria=categoria)
    return render(request, 'galeria/index.html', {'cards': fotografias})