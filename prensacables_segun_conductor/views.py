from django.shortcuts import render
from django.template import RequestContext, loader
from base_datos_medidas import Base_Datos_Medidas


def prensacables_segun_conductor(request):
    Base_Datos_Medidas.tabla_calculo_prensacable()
    if request.method == "POST":
        if request.POST.get("calcular_unipolar"):
            Base_Datos_Medidas.eliminar()
            Base_Datos_Medidas.alta_calculo_prensacable(request.POST.get("calcular_unipolar"))
        if request.POST.get("calcular_tpr"):
            Base_Datos_Medidas.eliminar()
            Base_Datos_Medidas.alta_calculo_prensacable(request.POST.get("calcular_tpr"))
        if request.POST.get("calcular_subterraneo"):
            Base_Datos_Medidas.eliminar()
            Base_Datos_Medidas.alta_calculo_prensacable(request.POST.get("calcular_subterraneo"))
        if request.POST.get("calcular_subterraneo_comando"):
            Base_Datos_Medidas.eliminar()
            Base_Datos_Medidas.alta_calculo_prensacable(request.POST.get("calcular_subterraneo_comando"))
        if request.POST.get("calcular_subterraneo_ls0h"):
            Base_Datos_Medidas.eliminar()
            Base_Datos_Medidas.alta_calculo_prensacable(request.POST.get("calcular_subterraneo_ls0h"))

    unipolar = Base_Datos_Medidas.entradas("unipolar")
    tpr = Base_Datos_Medidas.entradas("tpr")
    subterraneo = Base_Datos_Medidas.entradas("subterraneo")
    subterraneo_comando = Base_Datos_Medidas.entradas("subterraneo_comando")
    subterraneo_ls0h = Base_Datos_Medidas.entradas("subterraneo_ls0h")

    diametro = Base_Datos_Medidas.entradas("tabla_calculo_prensacable")[0][0]
    plastico_bsc = Base_Datos_Medidas.prensacable("plastico_bsc", diametro)
    plastico_bsp = Base_Datos_Medidas.prensacable("plastico_bsp", diametro)
    plastico_pg = Base_Datos_Medidas.prensacable("plastico_pg", diametro)
    metalico_bsc = Base_Datos_Medidas.prensacable("metalico_bsc", diametro)
    metalico_bsp = Base_Datos_Medidas.prensacable("metalico_bsp", diametro)
    metalico_pc = Base_Datos_Medidas.prensacable("metalico_pc", diametro)

    return render(request, "prensacables_segun_conductor/prensacables_segun_conductor.html",
                  {"plastico_bsc": plastico_bsc,
                   "plastico_bsp": plastico_bsp,
                   "plastico_pg": plastico_pg,
                   "metalico_bsc": metalico_bsc,
                   "metalico_bsp": metalico_bsp,
                   "metalico_pc": metalico_pc,
                   "unipolar": unipolar,
                   "tpr": tpr,
                   "subterraneo": subterraneo,
                   "subterraneo_comando": subterraneo_comando,
                   "subterraneo_ls0h": subterraneo_ls0h
                   }
                  )
