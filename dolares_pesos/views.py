from django.shortcuts import render
from django.template import RequestContext, loader
from forms import FormularioConversorPesosDolares
from forms import FormularioConversorDolaresPesos
from forms import FormularioDivisorCantidades
from base_datos import Base_Datos


def dolares_pesos(request):
    if request.method == "POST":
        formulario_conversor_dolares_pesos = FormularioConversorDolaresPesos(request.POST)
        if formulario_conversor_dolares_pesos.is_valid():
            cantidad_dp = int(formulario_conversor_dolares_pesos.cleaned_data["cantidad_dp"])
            total_dp = float(formulario_conversor_dolares_pesos.cleaned_data["total_dp"])
            tipo_cambio_dp = float(formulario_conversor_dolares_pesos.cleaned_data["tipo_cambio_dp"])
            print(cantidad_dp, total_dp, tipo_cambio_dp)
            Base_Datos.alta_dolares_pesos(cantidad_dp, total_dp, tipo_cambio_dp)

    if request.method == "GET":
        if request.GET.get("eliminar_dolares_pesos"):
            Base_Datos.eliminar("tabla_conversor_dolares_pesos", str(request.GET.get("eliminar_dolares_pesos")))

    formulario_conversor_dolares_pesos = FormularioConversorDolaresPesos()

    entradas_dolares_peses = Base_Datos.entradas("tabla_conversor_dolares_pesos")

    return render(request, "dolares_pesos/dolares_pesos.html",
                  {"formulario_conversor_dolares_pesos": formulario_conversor_dolares_pesos,
                   "entradas_dolares_pesos": entradas_dolares_peses}
                  )
