from django.urls import path
from . import views

urlpatterns = [
    path('mensajes/', views.MensajesList.as_view()),
    path('mensajes/<int:pk>/', views.MensajesDetail.as_view()),

    path('usuarios/', views.UsuariosList.as_view()),
    path('usuarios/<int:pk>/', views.UsuarioDetail.as_view()),
]
