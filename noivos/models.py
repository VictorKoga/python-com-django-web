from django.db import models
import secrets

# Cria o modelo para os convidados
class Convidados(models.Model):
    status_choices = (
        ('AC', 'Aguardando confirmação'),
        ('C', 'Confirmado'),
        ('R', 'Recusado')
    )

    nome_convidado = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=25, null=True, blank=True)
    maximo_acompanhantes = models.PositiveIntegerField(default=0)
    token = models.CharField(max_length=25, unique=True)  # Garantir que o token seja único
    status = models.CharField(max_length=2, choices=status_choices, default='AC')

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = secrets.token_urlsafe(16)
        super(Convidados, self).save(*args, **kwargs)

    @property
    def link_convite(self):
        return f'http://127.0.0.1:8000/convidados/?token={self.token}'

    def __str__(self):
        return self.nome_convidado
    
    # Cria o modelo para os presentes
class Presentes(models.Model):
    nome_presente = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='presentes')
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    importancia = models.IntegerField()
    reservado = models.BooleanField(default=False)
    reservado_por = models.ForeignKey(Convidados, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_presente
    
from django.db import models

class Acompanhantes(models.Model):
    convidado = models.ForeignKey(Convidados, on_delete=models.CASCADE, related_name='acompanhantes')
    nome = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f'{self.nome} - {self.whatsapp if self.whatsapp else "Sem WhatsApp"}'
