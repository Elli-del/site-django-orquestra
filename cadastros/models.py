from django.db import models

# Create your models here.
class Naipe(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Instrumento(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Musico(models.Model):
    VOZES = {
        '1a':'Primeira Voz',
        '2a':'Segunda Voz',
        '3a':'Terceira Voz'
    }
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField("nome do musico", max_length=100)
    data_nascimento = models.DateField()
    data_ingresso = models.DateField()
    naipe = models.ForeignKey(Naipe, on_delete=models.CASCADE)
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)
    voz = models.CharField("voz do instrumento", max_length=2, choices=VOZES, default='1a')
    foto = models.ImageField(upload_to='img/musicos', null=True, blank=True)

    def __str__(self):
        return self.nome
    