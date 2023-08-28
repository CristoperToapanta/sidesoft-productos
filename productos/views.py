import time
import requests
import base64
import json
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import render, redirect

def show_login(request):

    if request.method == 'POST':
        
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        
        url = 'https://obpreprod.sidesoftcorp.com/happypreprod//org.openbravo.service.json.jsonrest/MaterialMgmtStorageDetail'
        cabecera = {
           'Authorization': 'Basic ' + base64.b64encode(f'{usuario}:{password}'.encode()).decode()
        }
        
        response = requests.get(url, headers=cabecera)
        
        if response.status_code == 200:
            return redirect('get_productos', usuario=usuario, password=password)
        
    
    return render(request, 'login.html')


def get_productos(request, usuario, password):
    
    start_time = time.time()

    print(usuario)
    print(password)

    url = 'https://obpreprod.sidesoftcorp.com/happypreprod//org.openbravo.service.json.jsonrest/MaterialMgmtStorageDetail'
    cabecera = {
        'Authorization': 'Basic ' + base64.b64encode(f'{usuario}:{password}'.encode()).decode() 
    }

    response = requests.get(url, headers=cabecera)
    
    print('resp: ', response)

    if response.status_code == 200:
        productos = response.json()

        productos_json = json.dumps(productos)
        
        return render(request, 'menu.html', {'productos_json': productos_json})
    else:
        return JsonResponse({'error': 'Error al conectarse al ERP'}, status=500)
