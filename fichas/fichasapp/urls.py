from django.urls import path
from . import views

app_name = 'fichasapp'

urlpatterns  = [
    path('', views.home, name='index'),
    path('usuario/', views.usuarios, name='usuario'),
    path('crear_usuario/', views.crearUsuario, name='crear_usuario'), 
    path('modificar_usuario/<str:pk>', views.modificarUsuario, name='modificar_usuario'),
    path('eliminar_usuario/<str:pk>', views.eliminarUsuario, name='eliminar_usuario'), 
    path('mostrar_usuario/<str:pk>', views.mostrar_usuario, name='mostrar_usuario'), 
 
]