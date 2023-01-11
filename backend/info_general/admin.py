from django.contrib import admin
from .models import Servidor, Roteiro, Afastamento, Fds, Pedido

@admin.register(Servidor)
class ServidorAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'grupo', 'setor', 'parceiro')

@admin.register(Roteiro)
class RoteiroAdmin(admin.ModelAdmin):
    list_display = ('cod_roteiro', 'posto_base', 'descricao', 'data_registro')


@admin.register(Afastamento)
class AfastamentoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'motivo', 'data_inicio', 'data_fim', 'data_registro')

@admin.register(Fds)
class FdsAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'area', 'posto_base', 'equipamento', 'data', 'hora_entrada', 'hora_saida')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'solicitacao', 'data_inicio', 'data_fim', 'participantes', 'data_registro')
