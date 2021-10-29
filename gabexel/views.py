from django.shortcuts import render
from django.template import RequestContext, loader
from forms import FormularioGabinete
from base_datos_gabinetes import Base_Datos_Gabinete


def gabexel(request):
    if request.method == "POST":
        formulario_gabinete = FormularioGabinete(request.POST)
        if formulario_gabinete.is_valid():
            codigo_gabinete = int(formulario_gabinete.cleaned_data["codigo_gabinete"])
            print(codigo_gabinete)
            entradas_gabexel = Base_Datos_Gabinete.entradas_gabexel(codigo_gabinete)

    formulario_gabinete = FormularioGabinete()

    try:
        entradas_gabexel = Base_Datos_Gabinete.entradas_gabexel(codigo_gabinete)
    except UnboundLocalError:
        entradas_gabexel = []

    return render(request, "gabexel/gabexel.html",
                  {"formulario_gabinete": formulario_gabinete,
                   "entradas_gabexel": entradas_gabexel}
                  )
