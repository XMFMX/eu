from django.shortcuts import render
from django.template import RequestContext, loader
from forms import FormularioGabinete
from base_datos_gabinetes import Base_Datos_Gabinete


def genrod(request):
    if request.method == "POST":
        formulario_gabinete = FormularioGabinete(request.POST)
        if formulario_gabinete.is_valid():
            codigo_gabinete = int(formulario_gabinete.cleaned_data["codigo_gabinete"])
            print(codigo_gabinete)
            entradas_genrod_calado_abisagrado = Base_Datos_Gabinete.entradas_genrod_calado_abisagrado(codigo_gabinete)
            entradas_genrod_ciego_abisagrado = Base_Datos_Gabinete.entradas_genrod_ciego_abisagrado(codigo_gabinete)
            entradas_genrod_ciego_fijo = Base_Datos_Gabinete.entradas_genrod_ciego_fijo(codigo_gabinete)

    formulario_gabinete = FormularioGabinete()

    try:
        entradas_genrod_calado_abisagrado = Base_Datos_Gabinete.entradas_genrod_calado_abisagrado(codigo_gabinete)
        entradas_genrod_ciego_abisagrado = Base_Datos_Gabinete.entradas_genrod_ciego_abisagrado(codigo_gabinete)
        entradas_genrod_ciego_fijo = Base_Datos_Gabinete.entradas_genrod_ciego_fijo(codigo_gabinete)
    except UnboundLocalError:
        entradas_genrod_calado_abisagrado = []
        entradas_genrod_ciego_abisagrado = []
        entradas_genrod_ciego_fijo = []

    return render(request, "genrod/genrod.html",
                  {"formulario_gabinete": formulario_gabinete,
                   "entradas_genrod_calado_abisagrado": entradas_genrod_calado_abisagrado,
                   "entradas_genrod_ciego_abisagrado": entradas_genrod_ciego_abisagrado,
                   "entradas_genrod_ciego_fijo": entradas_genrod_ciego_fijo}
                  )
