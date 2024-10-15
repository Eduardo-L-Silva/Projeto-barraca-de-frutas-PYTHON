from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('login_vendedor/', views.login_vendedor, name='login_vendedor'),
    path('pagina_principal_vendedor/', views.pagina_principal_vendedor, name='pagina_principal_vendedor'),
    path('cadastrar_fruta/', views.cadastrar_fruta, name='cadastrar_fruta'),
    path('listar_frutas/', views.listar_frutas, name='listar_frutas'),
    path('vender_fruta/', views.vender_fruta, name='vender_fruta'),
    path('relatorio_vendas/', views.relatorio_vendas, name='relatorio_vendas'),
    path('pesquisar_frutas/', views.pesquisar_frutas, name='pesquisar_frutas'),
    path('filtrar_frutas/', views.filtrar_frutas, name='filtrar_frutas'),
    path('gerenciar/', views.gerenciar, name='gerenciar'),
    path('remover_fruta/<int:fruta_id>/', views.remover_fruta, name='remover_fruta'),
    path('remover_vendedor/<int:usuario_id>/', views.remover_vendedor, name='remover_vendedor'),
    path('remover_vendedor/<int:usuario_id>/', views.remover_vendedor, name='remover_vendedor'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Certifique-se de que este nome está correto
]
