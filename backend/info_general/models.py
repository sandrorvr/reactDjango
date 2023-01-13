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
    
    TUNO = [
        ('n','NOTURNO'),
        ('v','VESPERTINO'),
        ('m','MATUTINO'),
        ]
    matricula = models.CharField(max_length=7, primary_key=True)
    nome = models.CharField(max_length=120)
    grupo = models.CharField(max_length=1, choices=GRUPOS, blank=False)
    setor = models.CharField(max_length=5, choices=SETORES)
    turno = models.CharField(max_length=1, choices=TUNO, blank=False)

    def __str__(self):
        return self.nome

class Local(models.Model):
    AREA = [
        ('a1','AREA 1'),
        ('a2','AREA 2'),
        ('a3','AREA 3'),
        ('a4','AREA 4'),
        ('a5','AREA 5'),
        ('a6','AREA 6'),
        ('a7','AREA 7'),
        ('a8','AREA 8'),
        ('a9','AREA 9'),
        ('a10','AREA 10'),
        ('a11','AREA 11'),
        ]
    cod_local = models.AutoField(primary_key=True)
    posto_base = models.CharField(max_length=60)
    roteiro = models.TextField(max_length=500)
    area = models.CharField(max_length=3, choices=AREA, blank=False)


class Afastamento(models.Model):
    cod_afastamento = models.AutoField(primary_key=True)
    matricula = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    motivo = models.TextField(max_length=500)
    data_inicio = models.DateField(blank=False)
    data_fim = models.DateField(blank=False)
    data_registro = models.DateField(auto_now=True)


class Guarnica(models.Model):
    cod_guarnicao = models.AutoField(primary_key=True)
    data = models.DateField(null=False)
    parceiro_rx = models.ForeignKey(Servidor, on_delete=models.CASCADE, related_name='parceiro_rx')
    parceiro_tx = models.ForeignKey(Servidor, on_delete=models.CASCADE, related_name='parceiro_tx')

class Escala(models.Model):
    VEICULO = [
        ('vtr', 'VIATURA'),
        ('moto', 'MOTO'),
        ('po', 'PO')
    ]
    cod_escala = models.AutoField(primary_key=True)
    cod_guarnica = models.ForeignKey(Guarnica, on_delete=models.CASCADE)
    cod_local = models.ForeignKey(Local, on_delete=models.CASCADE)
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
