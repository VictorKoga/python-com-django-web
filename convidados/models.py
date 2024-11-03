from django.db import models

class Convidados(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    presente = models.ForeignKey('Presentes', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class Presentes(models.Model):
    nome_presente = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='presentes/')
    importancia = models.IntegerField()

    def __str__(self):
        return self.nome_presente
