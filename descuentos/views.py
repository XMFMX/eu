from django.shortcuts import render
from django.template import RequestContext, loader
from forms import FormularioDescuentos
from .descuentos import Descuentos


def descuentos(request):
    if request.method == "POST":
        formulario_descuentos = FormularioDescuentos(request.POST)
        if formulario_descuentos.is_valid():
            costo = float(formulario_descuentos.cleaned_data["costo"])
            desc0 = float(formulario_descuentos.cleaned_data["desc0"])
            desc1 = float(formulario_descuentos.cleaned_data["desc1"])
            desc2 = float(formulario_descuentos.cleaned_data["desc2"])
            desc3 = float(formulario_descuentos.cleaned_data["desc3"])
            desc4 = float(formulario_descuentos.cleaned_data["desc4"])
            desc5 = float(formulario_descuentos.cleaned_data["desc5"])
            desc6 = float(formulario_descuentos.cleaned_data["desc6"])
            desc7 = float(formulario_descuentos.cleaned_data["desc7"])
            desc8 = float(formulario_descuentos.cleaned_data["desc8"])
            desc9 = float(formulario_descuentos.cleaned_data["desc9"])
            renta = float(formulario_descuentos.cleaned_data["renta"])
            precio = Descuentos.precio(costo, desc0, desc1, desc2, desc3, desc4,
                                       desc5, desc6, desc7, desc8, desc9, renta)

    formulario_descuentos = FormularioDescuentos()

    try:
        precio = Descuentos.precio(costo, desc0, desc1, desc2, desc3, desc4, desc5, desc6, desc7, desc8, desc9, renta)
    except UnboundLocalError:
        precio = 0

    return render(request, "descuentos/descuentos.html", {"formulario_descuentos": formulario_descuentos,
                                                          "precio": precio})
