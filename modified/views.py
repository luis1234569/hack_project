from django.shortcuts import render

def modifies (request):
    lista = ['manzana', 'naranja', 'banana', 'pera']
    lista[0:2] =['verde', 'amarillo']
    lista += ['sandia', 'coco', 'limon']
    lista.append('apocalipsis')
    lista.extend(['familia','tornado'])
    del lista[4]
    lista.remove('amarillo')
    lista[0]= 'piña'
    lista.insert(0, 'estatus')
    lista.pop(5)
    lista.reverse()
    lista.sort()
    lista.sort(reverse=True)
    lista.append(lista.index('coco'))
    

    
    diccionario1 = {'camila': 'forma@gmail.com', 'teto':'teto@gmail.com', 'fer': 'fer@gmail.com'}
    
    diccionario = dict([
        ('nombre', 'evelyn'),
        ('Edad', 34),
        ('Documento', 175565783)
    ])
    
    diccionario = {
        'diccionarioActual': diccionario,
        'diccionarionuevo': diccionario1
    }
    
    diccionario['nombre']= 'tu ñaña'
    diccionario['direccion']= 'nose loco' 
    diccionario['keys'] = list(diccionario.keys())
    diccionario['values']= list(diccionario.values())
    diccionario.pop('keys')
    diccionario.popitem()
    diccionario['nada']= 4545
    diccionario2={'nadaw': 2024}
    diccionario.update(diccionario2)
    # diccionario.clear()
        
    
    tupla =('one', 'two','tree','four','one')
    lista.append(tupla.count('one'))
    context = {'lista': lista, 'diccionario': diccionario, 'tupla': tupla }
    

    return render(request, 'modified.html', context )


# for index, l in enumerate(lista):
#     print(index, l)
#0 5
#1 9
#2 10

# lista1 = [5, 9, 10]
# lista2 = ["Jazz", "Rock", "Djent"]
# for l1, l2 in zip(lista1, lista2):
#     print(l1, l2)
#5 Jazz
#9 Rock
#10 Djent

# lista1 = [5, 9, 10]
# for i in range(0, len(lista)):
#     print(lista1[i])
#5
#9
#10