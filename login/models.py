from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nomeFantasia = models.CharField(max_length=30, unique=True)


class MyUser(AbstractUser):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, db_column='empresa')
    propietarioAdministrador = models.BooleanField(default=True)
    assinatura = models.BooleanField(default=False)
    def __str__(self):
        return self.username

    pass


class Funcionario(models.Model):
    nomeCompleto = models.CharField(max_length=150)
    apelido = models.CharField(max_length=15)
    numeroTelefone =models.CharField(max_length=11) 
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE,db_column='user')
    setor = models.CharField(max_length=15)


class Veiculos(models.Model):
    id = models.AutoField(primary_key=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, db_column='empresa')
    propietario = models.CharField(max_length=150)
    motorista = models.CharField(max_length=150)
    tipoVeiculo = models.CharField(max_length=30)
    marcaVeiculo= models.CharField(max_length=30)
    placa = models.CharField(max_length=7)
    veiculo = models.CharField(max_length=15) #modelo do veiculo
    inicialKm= models.DecimalField(max_digits=8,decimal_places=2)
    Atualkm = models.DecimalField(max_digits=8, decimal_places=2)
    fabricado = models.CharField(max_length=4)
    datain = models.DateField(auto_created=True)
    cavaloMecanico=models.BooleanField(default=False)

    class Meta:
        ordering = ["-placa"]

    def __str__(self):
        return self.placa


class Abastecimento(models.Model):
    id = models.AutoField(primary_key=True)
    placa = models.ManyToManyField('Veiculos')
    propietario = models.ForeignKey(MyUser, on_delete=models.CASCADE, db_column='propietario')
    data = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    litros = models.DecimalField(max_digits=8, decimal_places=2)
    precolitro = models.DecimalField(max_digits=8, decimal_places=2)
    posto = models.CharField(max_length=25)
    tanquecheio = models.BooleanField()
    kmatual = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ["data"]

    def __str__(self):
        return self.data