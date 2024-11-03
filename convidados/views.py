from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from noivos.models import Convidados, Presentes, Acompanhantes

def convidados(request):
    token = request.GET.get('token')
    convidado = Convidados.objects.get(token=token)
    presentes = Presentes.objects.filter(reservado=False).order_by('-importancia')
    return render(request, 'convidados.html', {'convidado': convidado, 'presentes': presentes})

def responder_presenca(request):
    resposta = request.GET.get('resposta')
    token = request.GET.get('token')
    convidado = Convidados.objects.get(token=token)
    
    # Simplificando a verificação de resposta
    if resposta not in ['C', 'R']:
        messages.error(request, 'Você deve confirmar ou recusar')  # Simplificando a adição de mensagens
        return redirect(f'/convidados/?token={token}')  # Corrigindo a redireção
    
    convidado.status = resposta
    convidado.save()

    return redirect(f'/convidados/?token={token}')  # Corrigindo a redireção

def reservar_presente(request, id):
    token = request.GET.get('token')
    convidado = Convidados.objects.get(token=token)
    presente = Presentes.objects.get(id=id)
    
    presente.reservado = True
    presente.reservado_por = convidado
    presente.save()
    
    return redirect(f'/convidados/?token={token}')

def adicionar_acompanhante(request):
    if request.method == 'POST':
        token = request.POST.get('token')  # Obtém o token dos dados do POST
        # Garante que o convidado exista ou retorna 404
        convidado = get_object_or_404(Convidados, token=token)
        
        maximo_acompanhantes = convidado.maximo_acompanhantes

        # Verifica o número de acompanhantes existentes
        if convidado.acompanhantes.count() >= maximo_acompanhantes:
            messages.error(request, 'Você já atingiu o número máximo de acompanhantes')
            return redirect(f'/convidados/?token={token}')
        
        # Obtém dados do POST
        nome_acompanhante = request.POST.get('nome_acompanhante')
        whatsapp_acompanhante = request.POST.get('whatsapp_acompanhante')
        
        # Valida se o nome do acompanhante está presente
        if not nome_acompanhante:
            messages.error(request, 'O nome do acompanhante não pode estar vazio.')
            return redirect(f'/convidados/?token={token}')

        # Salva o acompanhante no banco de dados
        acompanhante = Acompanhantes(nome=nome_acompanhante, whatsapp=whatsapp_acompanhante, convidado=convidado)
        acompanhante.save()
        
        # Mensagem de sucesso e redirecionamento de volta à página de convidados
        messages.success(request, 'Acompanhante adicionado com sucesso!')
        return redirect(f'/convidados/?token={token}')
    
    # Caso não seja uma requisição POST
    messages.error(request, 'Método de solicitação inválido.')
    return redirect('convidados')  # Redireciona para uma página segura
