from datetime import date
from typing import Dict
from django.db.models.query import ValuesListIterable
from django.http import response
from django.shortcuts import redirect, render, HttpResponse
from django.views.generic import ListView
from login.forms import CadForm
from login.models import MyUser, Veiculos, Empresa, Funcionario


# Create your views here.


def index(request):
    return render(request, template_name="login/index.html")


def veiculos(request, user):
    if request.user.is_authenticated:
        prop: int = MyUser.objects.values_list(
            'id', flat=True).get(username=user)
        o = 0

        for vs in Veiculos.objects.filter(propietario=prop):
            o = o + 1
            print(o)

        if o > 0:

            return redirect('/publish')

        else:

            if request.method == "POST":
                form = CadForm(request.POST)
                if form.is_valid():
                    user = request.POST['user']
                    placa = request.POST['placa']
                    veiculo = request.POST['veiculo']
                    Atualkm = request.POST['Atualkm']
                    datain = date.today()
                    bd = Veiculos(propietario=MyUser.objects.get(id=prop),
                                  placa=placa, veiculo=veiculo, Atualkm=Atualkm, datain=datain)
                    bd.save()
                    return redirect('index')

            else:
                form = CadForm()

            context = {'form': form}
            return render(request, "login/veiculos.html", context)

    else:
        return redirect('login')


def register(request):

    empresaid = None
    if request.method == 'POST':

        tipodecadastro = request.POST['empresa1']
        inputnome = request.POST['inputnome']
        username = request.POST['inputUser']

        if tipodecadastro == "TRUE":
            inputnomefantasia = request.POST['inputNomeFantasia']
            bancoDeDadosEmpresa = Empresa(nomeFantasia=inputnomefantasia)
            bancoDeDadosEmpresa.save()
            empresaid = Empresa.objects.get(nomeFantasia=inputnomefantasia)
        else:
            bancoDeDadosEmpresa = Empresa(nomeFantasia=username)
            bancoDeDadosEmpresa.save()
            empresaid = Empresa.objects.get(nomeFantasia=username)

        email = request.POST['inputEmail']
        password = request.POST['inputPassword']
        MyUser.objects.create_user(empresa=empresaid, username=username, email=email, password=password,
                                   propietarioAdministrador=True, first_name=inputnome)
        return redirect('login')

    return render(request, "registration/register.html")


class PublisherListView(ListView):
    model = Veiculos


def testeEmpresaExiste(request, ab):
    try:
        bd = Empresa.objects.get(nomeFantasia=ab)
        return HttpResponse(True)
    except:
        return HttpResponse(False)


def testeUsuarioExiste(request, us):
    try:
        bd = MyUser.objects.get(username=us)
        print(bd)
        return HttpResponse(True)
    except:
        return HttpResponse(False)


def testeEmailExiste(request, em):
    try:
        bd = MyUser.objects.get(email=em)
        return HttpResponse(True)
    except:
        return HttpResponse(False)


def buscaMotorista(request, usuario):
    
    try:
        bd:int = MyUser.objects.values_list('empresa').get(username=usuario)
        colaborador = MyUser.objects.values_list('id',flat=True).filter(empresa=bd)
        response = []
        for e in colaborador:    
            try:
                cargo = Funcionario.objects.values_list('setor',flat=True).get(user=e)
                if cargo == 'Motorista':
                    nomeCompleto = Funcionario.objects.values_list('nomeCompleto',flat=True).get(user=e)
                    response.append(e)
                    response.append(';')
                    response.append(nomeCompleto)
                    response.append(';')
            except:
                pass   
                
        return HttpResponse(response)

    except:
        response = None
        return HttpResponse(response)


