from django.db import models

# Create your models here.
class Servico(models.Model):
    servico = models.CharField(max_length=50, verbose_name="Serviço")

    def __str__(self):
        return "%s" % (self.servico)

CARRO = (
    (0,"Unidade Móvel (NZ)"),
    (1,"Unidade Móvel (SM)"),
    (2,"Unidade Móvel (TP)"),
    (3,"Unidade Móvel (UN)"),
    (4,"Unidade Móvel (XH)"),
    (5,"Carro Próprio"),
)

class Timesheet(models.Model):
    data = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Data")
    entrada = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Hora Entrada")
    almoco = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name="Início do Almoço")
    almoco_fim = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name="Fim do Almoço")
    saida = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Hora de Saída")
    servico = models.ManyToManyField(Servico, verbose_name="Serviço")
    carro = models.IntegerField(choices=CARRO, null=True, blank=True, verbose_name="Viatura")
    zona = models.CharField(max_length=200, verbose_name="Zona")
    medico = models.CharField(max_length=200, verbose_name="Médico")
       
    def __str__(self):
        return "%s" % (self.data)
