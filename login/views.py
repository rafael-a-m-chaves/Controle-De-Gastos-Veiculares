from django.shortcuts import render, redirect
from login.forms import CadForm
from login.models import Veiculos
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
# Create your views here.


def index(request):
    return render(request, template_name="login/index.html")


def veiculos (request,user):

    if request.user.is_authenticated:
        prop:int = User.objects.values_list('id',flat=True).get(username=user)
        o = 0
        
        for vs in  Veiculos.objects.filter(propietario=prop):
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
                    bd = Veiculos(propietario = User.objects.get(id = prop),
                    placa=placa, veiculo=veiculo, Atualkm=Atualkm, datain=datain)
                    bd.save()
                    return redirect('index')

            else:
                form = CadForm()
            
            context= {'form' : form}
            return render(request,"login/veiculos.html",context)

    else:
        return redirect('login')



def register (request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']        
        User.objects.create_user(username, email, password)
        return redirect('login')
    
    return render(request,"registration/register.html")



class PublisherListView(ListView):
    model = Veiculos


