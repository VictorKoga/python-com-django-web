# noivos/views.py

from django.shortcuts import render, redirect
from django.contrib import messages  # Para exibir mensagens
from .models import Presentes, Convidados

def home_redirect(request):
    return redirect('/noivos/')  # Redireciona para a URL /noivos/

def home(request):
    if request.method == "GET":
        # Obtém todos os objetos da tabela Presentes do banco de dados.
        presentes = Presentes.objects.all()
        nao_reservado = Presentes.objects.filter(reservado=False).count()
        reservado = Presentes.objects.filter(reservado=True).count()
        data = [nao_reservado, reservado]
        
        # Renderiza a página 'home.html' com a lista de presentes.
        return render(request, 'home.html', {'presentes': presentes, 'data': data})

    elif request.method == "POST":
        # Obtém dados do formulário.
        nome_presente = request.POST.get('nome_presente')
        preco = request.POST.get('preco')
        importancia = request.POST.get('importancia')
        foto = request.FILES.get('foto')

        # Verifica se todos os campos obrigatórios estão preenchidos.
        if not nome_presente or not preco or not importancia or not foto:
            messages.error(request, 'Todos os campos são obrigatórios.')  # Mensagem de erro
            return redirect('home')

        try:
            # Converte o valor de importância para um número inteiro.
            importancia = int(importancia)

            # Verifica se o valor de importância está no intervalo entre 1 e 5.
            if importancia < 1 or importancia > 5:
                messages.error(request, 'A importância deve estar entre 1 e 5.')  # Mensagem de erro
                return redirect('home')

            # Verifica se o preço é um número válido
            if float(preco) < 0:
                messages.error(request, 'O preço deve ser um valor positivo.')  # Mensagem de erro
                return redirect('home')

            # Cria uma nova instância de Presentes e salva no banco de dados.
            presente = Presentes(
                nome_presente=nome_presente,
                preco=preco,
                importancia=importancia,
                foto=foto
            )
            presente.save()

            messages.success(request, 'Presente adicionado com sucesso!')  # Mensagem de sucesso
            return redirect('home')  # Redireciona após o salvamento

        except ValueError:
            messages.error(request, 'Verifique os dados inseridos.')  # Mensagem de erro em caso de falha na conversão
            return redirect('home')

def lista_convidados(request):
    if request.method == 'GET':
        convidados = Convidados.objects.all()
        return render(request, 'lista_convidados.html', {'convidados': convidados})

    elif request.method == 'POST':
        nome_convidado = request.POST.get('nome_convidado')
        whatsapp = request.POST.get('whatsapp')
        maximo_acompanhantes = request.POST.get('maximo_acompanhantes')

        # Verifica se todos os campos obrigatórios estão preenchidos.
        if not nome_convidado or not whatsapp or not maximo_acompanhantes:
            messages.error(request, 'Todos os campos são obrigatórios.')  # Mensagem de erro
            return redirect('lista_convidados')

        try:
            maximo_acompanhantes = int(maximo_acompanhantes)
            if maximo_acompanhantes <= 0:
                messages.error(request, 'O número de acompanhantes deve ser maior que 0.')  # Mensagem de erro
                return redirect('lista_convidados')

            # Cria uma nova instância de Convidados e salva no banco de dados.
            convidado = Convidados(
                nome_convidado=nome_convidado,
                whatsapp=whatsapp,
                maximo_acompanhantes=maximo_acompanhantes
            )
            convidado.save()

            messages.success(request, 'Convidado adicionado com sucesso!')  # Mensagem de sucesso
            return redirect('lista_convidados')  # Redireciona após o salvamento

        except ValueError:
            messages.error(request, 'Verifique os dados inseridos.')  # Mensagem de erro em caso de falha na conversão
            return redirect('lista_convidados')
