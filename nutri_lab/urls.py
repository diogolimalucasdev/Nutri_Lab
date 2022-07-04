"Definir as rotas da minha aplicação"
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('autenticacao.urls'))
]
