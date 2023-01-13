from django.contrib import admin
from .models import Servidor, Local, Afastamento, Escala, Pedido, Operacao

@admin.register(Servidor)
class ServidorAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'grupo', 'setor', 'turno')

@admin.register(Local)
class RoteiroAdmin(admin.ModelAdmin):
    list_display = ('cod_local', 'posto_base', 'roteiro', 'area')


@admin.register(Afastamento)
class AfastamentoAdmin(admin.ModelAdmin):
    list_display = ('cod_afastamento', 'servidor', 'motivo', 'descricao','data_inicio', 'data_fim', 'data_registro')

@admin.register(Escala)
class FdsAdmin(admin.ModelAdmin):
    list_display = ('cod_escala', 'servidor', 'local', 'equipamento', 'data', 'hora_entrada', 'hora_saida')

@admin.register(Operacao)
class OperacaoAdmin(admin.ModelAdmin):
    list_display = ('cod_operacao', 'nome', 'descricao', 'data')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cod_pedido','servidor', 'solicitacao', 'data_inicio', 'data_fim', 'data_registro')
