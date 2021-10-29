from django.shortcuts import render
from base_datos_medidas import Base_Datos_Medidas


def prensacables(request):
    plastico_bsc = Base_Datos_Medidas.entradas("plastico_bsc")
    plastico_bsp = Base_Datos_Medidas.entradas("plastico_bsp")
    plastico_pg = Base_Datos_Medidas.entradas("plastico_pg")
    metalico_bsc = Base_Datos_Medidas.entradas("metalico_bsc")
    metalico_bsp = Base_Datos_Medidas.entradas("metalico_bsp")
    metalico_pc = Base_Datos_Medidas.entradas("metalico_pc")
    return render(request, "prensacables/prensacables.html", {"plastico_bsc": plastico_bsc,
                                                              "plastico_bsp": plastico_bsp,
                                                              "plastico_pg": plastico_pg,
                                                              "metalico_bsc": metalico_bsc,
                                                              "metalico_bsp": metalico_bsp,
                                                              "metalico_pc": metalico_pc},)
