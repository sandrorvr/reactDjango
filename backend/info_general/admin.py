from django.contrib import admin
from .models import Servidor, Roteiro, Afinidade, Afastamento, Fds, Pedido

@admin.register(Servidor)
class ServidorAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'grupo', 'setor')

@admin.register(Roteiro)
class RoteiroAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'posto_base', 'roteiro', 'data_registro')

@admin.register(Afinidade)
class AfinidadeAdmin(admin.ModelAdmin):
    list_display = ('data_registro', 'matricula', 'matricula_rx', 'cod_roteiro')

@admin.register(Afastamento)
class AfastamentoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'motivo', 'data_inicio', 'data_fim', 'data_registro')

@admin.register(Fds)
class FdsAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'area', 'posto_base', 'equipamento', 'data', 'hora_entrada', 'hora_saida')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'solicitacao', 'data_inicio', 'data_fim', 'participantes', 'data_registro')
