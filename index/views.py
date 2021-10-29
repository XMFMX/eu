from django.shortcuts import render
from django.template import RequestContext, loader
from forms import FormularioConversorPesosDolares
from forms import FormularioConversorDolaresPesos
from forms import FormularioDivisorCantidades
from base_datos import Base_Datos


def index(request):
    if request.method == "POST":
        formulario_conversor_pesos_dolares = FormularioConversorPesosDolares(request.POST)
        if formulario_conversor_pesos_dolares.is_valid():
            cantidad_pd = int(formulario_conversor_pesos_dolares.cleaned_data["cantidad_pd"])
            total_pd = float(formulario_conversor_pesos_dolares.cleaned_data["total_pd"])
            tipo_cambio_pd = float(formulario_conversor_pesos_dolares.cleaned_data["tipo_cambio_pd"])
            print(cantidad_pd, total_pd, tipo_cambio_pd)
            Base_Datos.alta_pesos_dolares(cantidad_pd, total_pd, tipo_cambio_pd)

        formulario_conversor_dolares_pesos = FormularioConversorDolaresPesos(request.POST)
        if formulario_conversor_dolares_pesos.is_valid():
            cantidad_dp = int(formulario_conversor_dolares_pesos.cleaned_data["cantidad_dp"])
            total_dp = float(formulario_conversor_dolares_pesos.cleaned_data["total_dp"])
            tipo_cambio_dp = float(formulario_conversor_dolares_pesos.cleaned_data["tipo_cambio_dp"])
            print(cantidad_dp, total_dp, tipo_cambio_dp)
            Base_Datos.alta_dolares_pesos(cantidad_dp, total_dp, tipo_cambio_dp)

        formulario_divisor_cantidades = FormularioDivisorCantidades(request.POST)
        if formulario_divisor_cantidades.is_valid():
            cantidad_dc = int(formulario_divisor_cantidades.cleaned_data["cantidad_dc"])
            total_dc = float(formulario_divisor_cantidades.cleaned_data["total_dc"])
            print(cantidad_dc, total_dc)
            Base_Datos.alta_divisor_cantidades(cantidad_dc, total_dc)

    if request.method == "GET":
        if request.GET.get("eliminar_pesos_dolares"):
            Base_Datos.eliminar("tabla_conversor_pesos_dolares", str(request.GET.get("eliminar_pesos_dolares")))
        if request.GET.get("eliminar_dolares_pesos"):
            Base_Datos.eliminar("tabla_conversor_dolares_pesos", str(request.GET.get("eliminar_dolares_pesos")))
        if request.GET.get("eliminar_divisor_cantidades"):
            Base_Datos.eliminar("tabla_divisor_cantidades", str(request.GET.get("eliminar_divisor_cantidades")))

    formulario_conversor_pesos_dolares = FormularioConversorPesosDolares()
    formulario_conversor_dolares_pesos = FormularioConversorDolaresPesos()
    formulario_divisor_cantidades = FormularioDivisorCantidades()

    entradas_pesos_dolares = Base_Datos.entradas("tabla_conversor_pesos_dolares")
    entradas_dolares_peses = Base_Datos.entradas("tabla_conversor_dolares_pesos")
    entradas_divisor_cantidades = Base_Datos.entradas("tabla_divisor_cantidades")

    return render(request, "index/index.html",
                  {"formulario_conversor_pesos_dolares": formulario_conversor_pesos_dolares,
                   "formulario_conversor_dolares_pesos": formulario_conversor_dolares_pesos,
                   "formulario_divisor_cantidades": formulario_divisor_cantidades,
                   "entradas_pesos_dolares": entradas_pesos_dolares,
                   "entradas_dolares_pesos": entradas_dolares_peses,
                   "entradas_divisor_cantidades": entradas_divisor_cantidades}
                  )
