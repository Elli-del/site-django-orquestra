from django.shortcuts import render, redirect
from .forms import DiretoriaForm
from .models import Diretoria

# Create your views here.
def index (request):
    return render(request, 'index.html', {'nome': 'Fazendo Música'})

def historia (request):
    return render(request, 'historia.html', {'nome': 'Fazendo Música'})


def musicos (request):

    naipe_cordas = [
        {'nome': 'João da Silva', 'instrumento': 'Violino', 'foto': 'img/musicos/joao_silva.jpg'},
        {'nome': 'Maria Santos', 'instrumento': 'Baixo', 'foto': 'img/musicos/maria_santos.jpg'},
        {'nome': 'José Rocha', 'instrumento': 'Violoncelo', 'foto': 'img/musicos/jose_rocha.jpg'}
                    ]

    naipe_metais = [
        {'nome': 'João dos Sant"/home/ubuntu/back-end/orquestra/cadastros/views.py", line 3lva', 'instrumento': 'Bateria', 'foto': 'img/musicos/joaquim_silva.jpg'},
        {'nome': 'Pedro Santos', 'instrumento': 'Tímpano', 'foto': 'img/musicos/pedro_santos.jpg'}
                        ]
    
    naipes = [
        {'naipe': 'Cordas', 'musicos': naipe_cordas},
        {'naipe': 'Metais', 'musicos': naipe_metais},
        {'naipe': 'Percussão', 'musicos': naipe_percussao},
    ]

   

    return render(request, 'musicos.html', {'nome': 'Fazendo Música', 'naipes': naipes})

def diretoria(request):
    componentes = Diretoria.objects.all()
    return render(request, 'diretoria.html', {'componentes': componentes})

def cadastrar_diretoria(request):
    if request.method == 'POST':
        form = DiretoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diretoria')
    else:
        form = DiretoriaForm()
    return render(request, 'cadastrar_diretoria.html', {'form': form})
