from django.shortcuts import render

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
        {'nome': 'João dos Santos', 'instrumento': 'Trumpet', 'foto': 'img/musicos/joao_santos.jpg'},
        {'nome': 'José Silva', 'instrumento': 'Trombone', 'foto': 'img/musicos/jose_silva.jpg'},
        {'nome': 'Joaquim Rocha', 'instrumento': 'Tuba', 'foto': 'img/musicos/joaquim_rocha.jpg'}
                    ]

    naipe_percussao = [
        {'nome': 'Joaquim da Silva', 'instrumento': 'Bateria', 'foto': 'img/musicos/joaquim_silva.jpg'},
        {'nome': 'Pedro Santos', 'instrumento': 'Tímpano', 'foto': 'img/musicos/pedro_santos.jpg'}
                        ]
    
    naipes = [
        {'naipe': 'Cordas', 'musicos': naipe_cordas},
        {'naipe': 'Metais', 'musicos': naipe_metais},
        {'naipe': 'Percussão', 'musicos': naipe_percussao},
    ]



    return render(request, 'musicos.html', {'nome': 'Fazendo Música', 'naipes': naipes})
