from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('index.urls')),
    path('divisor_cantidades/', include('divisor_cantidades.urls')),
    path('dolares_pesos/', include('dolares_pesos.urls')),
    path('gabexel/', include('gabexel.urls')),
    path('genrod/', include('genrod.urls')),
    path('pesos_dolares/', include('pesos_dolares.urls')),
    path('medidas/', include('medidas.urls')),
    path('prensacables_segun_medida/', include('prensacables_segun_medida.urls')),
    path('prensacables_segun_conductor/', include('prensacables_segun_conductor.urls')),
    path('conductores/', include('conductores.urls')),
    path('canos/', include('canos.urls')),
    path('prensacables/', include('prensacables.urls')),
    path('descuentos/', include('descuentos.urls')),
    path('articulos/', include('articulos.urls')),
    path('admin/', admin.site.urls),
]
