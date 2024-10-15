from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import Fruta, Venda
from .forms import FrutaForm, UsuarioForm, EditFrutaForm
from django.db.models import Q
from .forms import UsuarioForm
from django.contrib.auth.models import User
from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Fruta
from .forms import FrutaForm, UsuarioForm, EditFrutaForm
from django.contrib.auth.models import User


# Página inicial
def index(request):
    return render(request, 'index.html')

@login_required
def pagina_principal_vendedor(request):
    return render(request, 'pagina_principal_vendedor.html')

# Funções para login
def login_admin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:
                auth_login(request, user)
                return redirect('gerenciar')  # Redireciona para a página de gerenciamento
            else:
                return redirect('index')  # Caso não seja admin, redirecionar para a página inicial
    else:
        form = AuthenticationForm()
    return render(request, 'login_admin.html', {'form': form})

def login_vendedor(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if not user.is_superuser:
                auth_login(request, user)
                return redirect('pagina_principal_vendedor')
            else:
                return redirect('index')  # Caso não seja vendedor, redirecionar para index ou outra página
    else:
        form = AuthenticationForm()
    return render(request, 'login_vendedor.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def gerenciar(request):
    fruta_form = FrutaForm()
    edit_fruta_form = EditFrutaForm()
    usuario_form = UsuarioForm()  # Formulário de Usuário

    if request.method == 'POST':
        if 'add_vendedor' in request.POST:
            usuario_form = UsuarioForm(request.POST)
            if usuario_form.is_valid():
                usuario = usuario_form.save(commit=False)
                usuario.is_staff = True
                usuario.save()
                return redirect('gerenciar')

        # Remover Vendedor
        elif 'remove_vendedor' in request.POST:
            usuario_id = request.POST.get('usuario_id')
            usuario = get_object_or_404(User, pk=usuario_id)
            if usuario:
                usuario.delete()
                return redirect('gerenciar')

        # Adicionar Fruta
        elif 'add_fruta' in request.POST:
            fruta_form = FrutaForm(request.POST)
            if fruta_form.is_valid():
                fruta_form.save()
                return redirect('gerenciar')

        # Remover Fruta
        elif 'remove_fruta' in request.POST:
            fruta_id = request.POST.get('fruta_id')
            fruta = get_object_or_404(Fruta, pk=fruta_id)
            if fruta:
                fruta.delete()
                return redirect('gerenciar')

        # Editar Fruta
        elif 'edit_fruta' in request.POST:
            fruta_id = request.POST.get('fruta_id')
            fruta = get_object_or_404(Fruta, pk=fruta_id)
            edit_fruta_form = EditFrutaForm(request.POST, instance=fruta)
            if edit_fruta_form.is_valid():
                edit_fruta_form.save()
                return redirect('gerenciar')

    frutas = Fruta.objects.all()
    vendedores = User.objects.filter(is_staff=True)

    context = {
        'fruta_form': fruta_form,
        'edit_fruta_form': edit_fruta_form,
        'usuario_form': usuario_form,  # Adicione o formulário ao contexto
        'frutas': frutas,
        'vendedores': vendedores,
    }
    return render(request, 'gerenciar.html', context)



@login_required
def vender_fruta(request):
    if request.method == 'POST':
        fruta_id = request.POST.get('fruta_id')
        quantidade = int(request.POST.get('quantidade'))
        desconto = int(request.POST.get('desconto', 0))

        fruta = get_object_or_404(Fruta, pk=fruta_id)

        if quantidade <= fruta.quantidade:
            valor_total = Decimal(fruta.valor) * Decimal(quantidade)
            valor_total -= valor_total * (Decimal(desconto) / Decimal(100))
            fruta.quantidade -= quantidade
            fruta.save()

            venda = Venda(
                fruta=fruta,
                quantidade=quantidade,
                valor_total=valor_total,
                desconto=desconto,
                vendedor=request.user
            )
            venda.save()

            return redirect('relatorio_vendas')
        else:
            return render(request, 'vender_fruta.html', {
                'error': 'Quantidade disponível insuficiente.',
                'frutas': Fruta.objects.all(),
            })
    else:
        frutas = Fruta.objects.all()
        return render(request, 'vender_fruta.html', {'frutas': frutas})

@login_required
def pesquisar_frutas(request):
    query = request.GET.get('q', '')
    frutas = Fruta.objects.filter(
        Q(nome__icontains=query) | Q(classificacao__icontains=query)
    )
    return render(request, 'pesquisar_frutas.html', {'frutas': frutas, 'query': query})

@login_required
def filtrar_frutas(request):
    classificacao = request.GET.get('classificacao', '')
    fresca = request.GET.get('fresca', '')

    frutas = Fruta.objects.all()
    if classificacao:
        frutas = frutas.filter(classificacao=classificacao)
    if fresca:
        fresca = True if fresca.lower() == 'sim' else False
        frutas = frutas.filter(fresca=fresca)

    return render(request, 'filtrar_frutas.html', {'frutas': frutas})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def cadastrar_fruta(request):
    if request.method == 'POST':
        form = FrutaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_principal_vendedor')
    else:
        form = FrutaForm()
    return render(request, 'cadastrar_fruta.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def listar_frutas(request):
    frutas = Fruta.objects.all()
    return render(request, 'listar_frutas.html', {'frutas': frutas})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def remover_fruta(request, fruta_id):
    fruta = get_object_or_404(Fruta, pk=fruta_id)
    if request.method == 'POST':
        fruta.delete()
        return redirect('listar_frutas')
    return render(request, 'remover_fruta.html', {'fruta': fruta})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def remover_vendedor(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('gerenciar')  # Redireciona para a página de gerenciamento após remover
    return render(request, 'remover_vendedor.html', {'usuario': usuario})

@login_required
def relatorio_vendas(request):
    vendas = Venda.objects.filter(vendedor=request.user).order_by('-horario')
    return render(request, 'relatorio_vendas.html', {'vendas': vendas})
