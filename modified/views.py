from django.shortcuts import render

def modifies (request):
    lista = ['manzana', 'naranja', 'banana', 'pera']
    lista.reverse()
    lista.sort()
    diccionario = {'camila': 'forma@gmail.com', 'teto':'teto@gmail.com', 'fer': 'fer@gmail.com'}
    tupla =('one', 'two','tree','four')
    context = {'lista': lista, 'diccionario': diccionario, 'tupla': tupla }
    

    return render(request, 'modified.html', context )

