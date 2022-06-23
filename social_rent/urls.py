from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

# from django.contrib.auth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('special_equipment/', include('special_equipment.urls')),

    path('', RedirectView.as_view(url='special_equipment/', permanent=True)),
    #  redirekt paaskinimas path('koki adresa peradresuojam', redirekto django funkcija...(url='i koki adresa redirektas/), permanent=True <- pastovus redirectas, naudingas broseriui, paieskoms ir kt)),
] + (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

