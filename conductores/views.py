from django.shortcuts import render
from base_datos_medidas import Base_Datos_Medidas


def conductores(request):
    unipolar = Base_Datos_Medidas.entradas("unipolar")
    tpr = Base_Datos_Medidas.entradas("tpr")
    subterraneo = Base_Datos_Medidas.entradas("subterraneo")
    subterraneo_comando = Base_Datos_Medidas.entradas("subterraneo_comando")
    subterraneo_ls0h = Base_Datos_Medidas.entradas("subterraneo_ls0h")
    return render(request, "conductores/conductores.html", {"unipolar": unipolar,
                                                            "tpr": tpr,
                                                            "subterraneo": subterraneo,
                                                            "subterraneo_comando": subterraneo_comando,
                                                            "subterraneo_ls0h": subterraneo_ls0h},)
