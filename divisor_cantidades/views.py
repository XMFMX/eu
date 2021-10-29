from django.shortcuts import render
from django.template import RequestContext, loader
from forms import FormularioDivisorCantidades
from base_datos import Base_Datos


def divisor_cantidades(request):
    if request.method == "POST":
        formulario_divisor_cantidades = FormularioDivisorCantidades(request.POST)
        if formulario_divisor_cantidades.is_valid():
            cantidad_dc = int(formulario_divisor_cantidades.cleaned_data["cantidad_dc"])
            total_dc = float(formulario_divisor_cantidades.cleaned_data["total_dc"])
            print(cantidad_dc, total_dc)
            Base_Datos.alta_divisor_cantidades(cantidad_dc, total_dc)

    if request.method == "GET":
        if request.GET.get("eliminar_divisor_cantidades"):
            Base_Datos.eliminar("tabla_divisor_cantidades", str(request.GET.get("eliminar_divisor_cantidades")))

    formulario_divisor_cantidades = FormularioDivisorCantidades()

    entradas_divisor_cantidades = Base_Datos.entradas("tabla_divisor_cantidades")

    return render(request, "divisor_cantidades/divisor_cantidades.html",
                  {"formulario_divisor_cantidades": formulario_divisor_cantidades,
                   "entradas_divisor_cantidades": entradas_divisor_cantidades}
                  )
