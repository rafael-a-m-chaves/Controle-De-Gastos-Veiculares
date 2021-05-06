from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Empresa (models.Model):
    id = models.AutoField(primary_key=True)
    nomeFantasia = models.CharField(max_length=30, unique=True)



class MyUser(AbstractUser):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, db_column='empresa')
    propietarioAdministrador = models.BooleanField(default=True)
    assinatura = models.BooleanField(default=False)
    pass



class Veiculos (models.Model):
    id = models.AutoField(primary_key=True)
    propietario =  models.ForeignKey(MyUser, on_delete=models.CASCADE, db_column='propietario')
    placa = models.CharField(max_length=7)
    veiculo = models.CharField(max_length=15)
    Atualkm = models.DecimalField(max_digits=8, decimal_places=2)
    datain = models.DateField(auto_created=True)
    
    class Meta:
        ordering = ["-placa"]


    def __str__(self):
        return self.placa



class Abastecimento (models.Model):
    id = models.AutoField(primary_key=True)
    placa = models.ManyToManyField('Veiculos')
    propietario = models.ForeignKey(MyUser,on_delete=models.CASCADE, db_column='propietario')
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

