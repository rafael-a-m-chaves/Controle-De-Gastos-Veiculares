from django.urls import path
from login import views
from login.views import PublisherListView


urlpatterns = [
    path('', views.index, name='index'),
    path('veiculos/?P', views.veiculos, name='veiculos'),
    path('veiculos/', views.veiculos, name='veiculos'),
    path('veiculos/<str:user>/', views.veiculos, name='veiculos'),
    path('registration',views.register, name='register'),
    path('publish', PublisherListView.as_view()),
    path('publish/', PublisherListView.as_view()), 
    path('testeEmpresaExiste/<str:ab>',views.testeEmpresaExiste),
    path('testeUsuarioExiste/<str:us>',views.testeUsuarioExiste),
    path('testeEmailExiste/<str:em>',views.testeEmailExiste),
]