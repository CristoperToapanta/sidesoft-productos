from django.urls import path
from . import views

urlpatterns = [
    path('getProductos/<str:usuario>/<str:password>/', views.get_productos, name='get_productos'),
    path('showLogin/', views.show_login, name='show_login')
]