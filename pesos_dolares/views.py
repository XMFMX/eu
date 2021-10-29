from django.shortcuts import render
from django.template import RequestContext, loader
from forms import FormularioConversorPesosDolares
from base_datos import Base_Datos


def pesos_dolares(request):
    if request.method == "POST":
        formulario_conversor_pesos_dolares = FormularioConversorPesosDolares(request.POST)
        if formulario_conversor_pesos_dolares.is_valid():
            cantidad_pd = int(formulario_conversor_pesos_dolares.cleaned_data["cantidad_pd"])
            total_pd = float(formulario_conversor_pesos_dolares.cleaned_data["total_pd"])
            tipo_cambio_pd = float(formulario_conversor_pesos_dolares.cleaned_data["tipo_cambio_pd"])
            print(cantidad_pd, total_pd, tipo_cambio_pd)
            Base_Datos.alta_pesos_dolares(cantidad_pd, total_pd, tipo_cambio_pd)

    if request.method == "GET":
        if request.GET.get("eliminar_pesos_dolares"):
            Base_Datos.eliminar("tabla_conversor_pesos_dolares", str(request.GET.get("eliminar_pesos_dolares")))

    formulario_conversor_pesos_dolares = FormularioConversorPesosDolares()

    entradas_pesos_dolares = Base_Datos.entradas("tabla_conversor_pesos_dolares")

    return render(request, "pesos_dolares/pesos_dolares.html",
                  {"formulario_conversor_pesos_dolares": formulario_conversor_pesos_dolares,
                   "entradas_pesos_dolares": entradas_pesos_dolares}
                  )
