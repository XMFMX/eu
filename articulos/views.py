from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import JsonResponse
from forms import FormularioArticulos
from .forms import *
from base_articulos import BaseArticulos


def articulos(request):
    """tsm_tipo = BaseArticulos.tsm_tipo
    tsm_subtipo_marca = BaseArticulos.tsm_subtipo_marca
    tipo_articulo = []
    subtipo_articulo = []
    marca_articulo = []
    ls = []
    lm = []
    for x in tsm_tipo:
        tupla = (x, x)
        tipo_articulo.append(tupla)
    for x in tsm_subtipo_marca:
        for y in x[0]:
            ls.append(y)
        for y in x[1]:
            lm.append(y)
    print(ls)
    print(lm)
    for x in ls:
        tupla_s = (x, x)
        subtipo_articulo.append(tupla_s)
    for x in lm:
        tupla_m = (x, x)
        marca_articulo.append(tupla_m)
    print(tipo_articulo[-1])
    print(subtipo_articulo[-1])
    print(marca_articulo[-1])
"""
    if request.method == "POST":
        formulario_articulos = FormularioArticulos(request.POST)
        if formulario_articulos.is_valid():
            tipo = float(formulario_articulos.cleaned_data["tipo"])
            subtipo = float(formulario_articulos.cleaned_data["subtipo"])
            marca = float(formulario_articulos.cleaned_data["marca"])

    formulario_articulos = FormularioArticulos()

    try:
        lista_articulos = BaseArticulos.entradas("marca")
    except UnboundLocalError:
        lista_articulos = BaseArticulos.entradas("marca")

    return render(request, "articulos/eu.html", {"formulario_articulos": formulario_articulos,
                                                 "lista_articulos": lista_articulos})


def conseguir_subtipo(request):
    tipo = request.POST.get('tipo')
    subtipo = subtipo_por_tipo(tipo)
    return JsonResponse({'subtipo': subtipo})
