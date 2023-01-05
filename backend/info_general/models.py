from django.db import models

class Servidor(models.Model):
    GRUPOS = [
        ('1','Grupo I'),
        ('2','Grupo II'),
        ('3','Grupo III'),
        ('4','Grupo IV')
        ]
    SETORES = [
        ('sefit','SEFIT'),
        ('sevop','SEVOP'),
        ('selve','SELVE'),
        ('areas','AREA'),
        ('coesp','COESP'),
        ('gasup','GASUP'),
        ('geren', 'GERENCIA')
        ]
    matricula = models.CharField(max_length=7)
    nome = models.CharField(max_length=120)
    grupo = models.CharField(max_length=1, choices=GRUPOS, blank=False)
    setor = models.CharField(max_length=25, choices=SETORES)

class Roteiro(models.Model):
    matricula = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    posto_base = models.CharField(max_length=120)
    roteiro = models.TextField(max_length=500)
    data_registro = models.DateField(auto_now=True)


class Afinidade(models.Model):
    data_registro = models.DateField(auto_now=True)
    matricula = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    matricula_rx = models.CharField(max_length=7, blank=False)
    cod_roteiro = models.ForeignKey(Roteiro, on_delete=models.CASCADE, blank=True)

class Afastamento(models.Model):
    matricula = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    motivo = models.TextField(max_length=500)
    data_inicio = models.DateField(blank=False)
    data_fim = models.DateField(blank=False)
    data_registro = models.DateField(auto_now=True)

class Fds(models.Model):
    VEICULO = [
        ('vtr', 'VIATURA'),
        ('moto', 'MOTO'),
        ('po', 'PO')
    ]
    matricula = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    area = models.CharField(max_length=50, blank=False)
    posto_base = models.CharField(max_length=80)
    equipamento = models.CharField(max_length=5, choices=VEICULO)
    data = models.DateField()
    hora_entrada = models.TimeField()
    hora_saida = models.TimeField()

class Pedido(models.Model):
    matricula = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    solicitacao = models.TextField(max_length=500, blank=False)
    data_inicio = models.DateField(blank=False)
    data_fim = models.DateField(blank=False)
    participantes = models.TextField(max_length=500, blank=False)
    data_registro = models.DateField(auto_now=True)

