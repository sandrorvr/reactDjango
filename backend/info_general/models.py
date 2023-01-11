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
    parceiro = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome

class Area(models.Model):
    cod_area = models.CharField(max_length=5, primary_key=True)
    nome = models.CharField(max_length=60)
    descricao = models.TextField(max_length=500)
    data_registro = models.DateField(auto_now=True)

class Roteiro(models.Model):
    cod_roteiro = models.CharField(max_length=5, primary_key=True)
    posto_base = models.CharField(max_length=120)
    descricao = models.TextField(max_length=500)
    data_registro = models.DateField(auto_now=True)


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
