from django.contrib import admin
from .models import Servidor, Local, Afastamento, Escala, Pedido, Guarnica

@admin.register(Servidor)
class ServidorAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'grupo', 'setor', 'turno')

@admin.register(Local)
class RoteiroAdmin(admin.ModelAdmin):
    list_display = ('cod_local', 'posto_base', 'roteiro', 'area')


@admin.register(Afastamento)
class AfastamentoAdmin(admin.ModelAdmin):
    list_display = ('cod_afastamento', 'matricula', 'motivo', 'data_inicio', 'data_fim', 'data_registro')

@admin.register(Escala)
class FdsAdmin(admin.ModelAdmin):
    list_display = ('cod_escala', 'cod_guarnica', 'cod_local', 'equipamento', 'data', 'hora_entrada', 'hora_saida')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'solicitacao', 'data_inicio', 'data_fim', 'participantes', 'data_registro')


@admin.register(Guarnica)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cod_guarnicao', 'data', 'parceiro_tx', 'parceiro_rx')
