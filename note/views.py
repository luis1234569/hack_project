from django.shortcuts import render

# Create your views here.
def joda(request):
    productos = ['Camisa', 'Pantalón', 'Zapatos', 'Bolso', 'Sombrero']
    productos.append('Corbata')
    
    inventario = {
    'Camisa': {'cantidad': 50, 'precio_unitario': 25.0},
    'Pantalón': {'cantidad': 30, 'precio_unitario': 40.0},
    'Zapatos': {'cantidad': 20, 'precio_unitario': 60.0},
    'Bolso': {'cantidad': 40, 'precio_unitario': 35.0},
    'Sombrero': {'cantidad': 25, 'precio_unitario': 20.0}
    }
    
    inventario2 = {
    'Sucursal A': {
        'Camisa': {'cantidad': 50, 'precio_unitario': 25.0},
        'Pantalón': {'cantidad': 30, 'precio_unitario': 40.0},
        'Zapatos': {'cantidad': 20, 'precio_unitario': 60.0}
    },
    'Sucursal B': {
        'Camisa': {'cantidad': 40, 'precio_unitario': 30.0},
        'Pantalón': {'cantidad': 35, 'precio_unitario': 45.0},
        'Bolso': {'cantidad': 25, 'precio_unitario': 35.0}
    },
    'Sucursal C': {
        'Zapatos': {'cantidad': 50, 'precio_unitario': 55.0},
        'Bolso': {'cantidad': 30, 'precio_unitario': 40.0},
        'Sombrero': {'cantidad': 20, 'precio_unitario': 20.0}
    }
}
    
    
    inventario2['Sucursal A']['Corbata']= {'cantidad': 15, 'precio_unitario': 30.0}
    inventario2['Sucursal B']['Camisa']['cantidad']=90  

    inventario['Corbata']= {
        'cantidad': 15,
        'precio_unitario': 30.0
    }
    inventario.pop('Sombrero')

    
    

    elements = productos
    
    diccionario= inventario2
    
    context={
        'elements': elements,
        'diccionario': diccionario 
    }
    return render(request, 'note.html', context)