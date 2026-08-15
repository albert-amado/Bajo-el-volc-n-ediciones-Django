from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static as static_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path("noticias/", include("noticias.urls")), 
    path('catalogo/', include('catalogo.urls')),
] + static_urls(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
