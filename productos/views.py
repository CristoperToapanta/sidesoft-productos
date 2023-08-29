import time
import requests
import base64
import json
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import render, redirect

def show_login(request):
    
    login = [
        {
            "user": "Openbravo",
            "password": "1234"
        }
    ]

    if request.method == 'POST':
        
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')

        if usuario is not None and password is not None:
            
            for account in login:
                
                if account["user"] == usuario and account["password"] == password:
                    return redirect('get_productos', usuario=usuario, password=password)
                
            else:
                return render(request, 'login.html')
            
        else:
            return render(request, 'login.html')
    
    return render(request, 'login.html')

def get_productos(request, usuario, password):
    
    url = 'https://obpreprod.sidesoftcorp.com/happypreprod//org.openbravo.service.json.jsonrest/MaterialMgmtStorageDetail'
    cabecera = {
        'Authorization': 'Basic ' + base64.b64encode(f'{usuario}:{password}'.encode()).decode() 
    }

    response = requests.get(url, headers=cabecera)
    
    if response.status_code == 200:
        
        productos = response.json()
        productos_json = json.dumps(productos)
        
        return render(request, 'menu.html', {'productos_json': productos_json})
    else:
        return JsonResponse({'error': 'Error al conectarse al ERP'}, status=500)
