from django.http import JsonResponse
from .models import Cliente, finalizar_compra

def finalizar_compra_view(request, cliente_id):
    # Chame a função finalizar_compra e retorne uma resposta
    cliente = Cliente.objects.get(id=cliente_id)
    finalizar_compra(cliente_id)
    return JsonResponse({'message': f'Compra finalizada para o cliente {cliente.nome}!'})
