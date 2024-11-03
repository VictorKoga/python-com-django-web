from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

# View para redirecionar a raiz para /noivos/
def home_redirect(request):
    return redirect('/noivos/')  # Redireciona para a URL /noivos/

urlpatterns = [
    path('', home_redirect, name='home_redirect'),  # Adiciona esta linha
    path('admin/', admin.site.urls),
    path('noivos/', include('noivos.urls')),
    path('convidados/', include('convidados.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
