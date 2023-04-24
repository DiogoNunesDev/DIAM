from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from store.models import Produto, Utilizador, Staff
from django.urls import reverse
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'home.html')

def full_collection(request):
    product_list = Produto.objects.all()
    context = {'product_list': product_list}
    return render(request, 'full_collection.html', context)

def cart_view(request):
    return render(request, 'cart.html')


def login_view(request):

    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            # reverse: quando estou dentro dos templates vai procurar o index e vai gerar o url correspondente
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'login.html', {'msg_erro':'Credenciais inválidas, tente novamente.'})
    else:
        #Mostrar o formulario de login
        return render(request, 'login.html')


def redirectLogin(request):
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def signup_view(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=name, password=password, email=email)
        user.save()
        primeiro_nome = request.POST['primeiro_nome']
        apelido = request.POST['apelido']
        data_nascimento = request.POST['data_nascimento']
        morada = request.POST['morada']
        numero_telemovel = request.POST['numero_telemovel']
        num_cartao_cidadao = request.POST['num_cartao_cidadao']
        nif = request.POST['nif']
        utilizador = Utilizador(user=user, primeiro_nome=primeiro_nome, apelido=apelido, data_nascimento=data_nascimento, morada=morada,
                                numero_telemovel=numero_telemovel, num_cartao_cidadao=num_cartao_cidadao, nif=nif, num_pontos=0, email=email)
        utilizador.save()
        login(request, user)
        return render(request, 'home.html')


def redirectSignup(request):
    return render(request, 'signup.html')


def addStaff(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=name, password=password, email=email)
        user.save()
        primeiro_nome = request.POST['primeiro_nome']
        apelido = request.POST['apelido']
        data_nascimento = request.POST['data_nascimento']
        morada = request.POST['morada']
        numero_telemovel = request.POST['numero_telemovel']
        num_cartao_cidadao = request.POST['num_cartao_cidadao']
        staff = Staff(user=user, primeiro_nome=primeiro_nome, apelido=apelido, data_nascimento=data_nascimento, morada=morada,
                        numero_telemovel=numero_telemovel, num_cartao_cidadao=num_cartao_cidadao, email=email)
        staff.save()
        return render(request, 'home.html')
    return render(request, 'addStaff.html')

def redirectAddStaff(request):
    return render(request, 'addStaff.html')


def profile(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html', {'msg_erro':'Utilizador não autenticado'})

    return render(request, 'profile.html')

def addProduct(request):
    if request.user.staff:
        tamanho = request.POST['tamanho']
        cor = request.POST['cor']
        preco = request.POST['preco']
        num_pontos = request.POST['num_pontos']
        categoria = request.POST['categoria']
        referencia = request.POST['referencia']
        Produto.makeProduct(tamanho, cor, preco, num_pontos, categoria)
    else:
        return redirect('login_view')

def redirectAddProduct(request):
    return render(request, 'addProduct.html')


def sweatshirts_view(request):
    product_list = Produto.objects.filter(categoria='Sweatshirt').order_by('cor')
    arr_produto_unico = []
    cores_vistas = set()
    for product in product_list:
        if product.cor not in cores_vistas:
            cores_vistas.add(product.cor)
            arr_produto_unico.append(product)
    context = {'product_list': arr_produto_unico}
    return render(request, 'sweatshirts.html', context)


def tshirts_view(request):
    product_list = Produto.objects.filter(categoria='T-Shirt').order_by('cor')
    arr_produto_unico = []
    cores_vistas = set()
    for product in product_list:
        if product.cor not in cores_vistas:
            cores_vistas.add(product.cor)
            arr_produto_unico.append(product)
    context = {'product_list': arr_produto_unico}
    return render(request, 'sweatshirts.html', context)

def detail_view(request,produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    context={'produto': produto}
    return render(request,'detail.html',context)

def redirectEditProfile(request):
    return render(request, 'editProfile.html')

def edit_profile(request):
    if request.method == 'POST':
        utilizador = request.user.utilizador
        user = request.user
        user.email = request.POST['email']
        user.save()
        utilizador.primeiro_nome = request.POST['primeiro_nome']
        utilizador.apelido = request.POST['apelido']
        utilizador.data_nascimento = request.POST['data_nascimento']
        utilizador.morada = request.POST['morada']
        utilizador.email = request.POST['email']
        utilizador.numero_telemovel = request.POST['numero_telemovel']
        utilizador.num_cartao_cidadao = request.POST['num_cartao_cidadao']
        utilizador.nif = request.POST['nif']
        utilizador.save()
        return render(request, 'profile.html')
    else:
        return render(request, 'edit_profile.html')


"""
NÃO APAGUEM ISTO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def edit_profile(request):
    if request.method == 'POST':
        utilizador = request.user.utilizador
        user = request.user
        if request.POST.get('email', '') != '':
            user.email = request.POST['email']
            user.save()
        if request.POST.get('primeiro_nome', '') != '':
            utilizador.primeiro_nome = request.POST['primeiro_nome']
        if request.POST.get('apelido', '') != '':
            utilizador.apelido = request.POST['apelido']
        if request.POST.get('data_nascimento', '') != '':
            utilizador.data_nascimento = request.POST['data_nascimento']
        if request.POST.get('morada', '') != '':
            utilizador.morada = request.POST['morada']
        if request.POST.get('numero_telemovel', '') != '':
            utilizador.numero_telemovel = request.POST['numero_telemovel']
        if request.POST.get('num_cartao_cidadao', '') != '':
            utilizador.num_cartao_cidadao = request.POST['num_cartao_cidadao']
        if request.POST.get('nif', '') != '':
            utilizador.nif = request.POST['nif']
        utilizador.save()
        return render(request, 'profile.html')
    else:
        return render(request, 'edit_profile.html')
"""