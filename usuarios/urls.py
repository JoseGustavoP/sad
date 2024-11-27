from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, AlterarSenhaView, minha_view_de_logout

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html'
    ), name="login"),
    
    path('logout/', minha_view_de_logout, name='logout'),
    
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),

    path('alterar-senha/', AlterarSenhaView.as_view(), name='alterar_senha'),
]