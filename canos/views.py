from django.shortcuts import render
from base_datos_medidas import Base_Datos_Medidas


def canos(request):
    plastico_sp = Base_Datos_Medidas.entradas("canos_plasticos_sp")
    plastico_ep = Base_Datos_Medidas.entradas("canos_plasticos_ep")
    plastico_lh = Base_Datos_Medidas.entradas("canos_plasticos_lh")
    hierro_liv = Base_Datos_Medidas.entradas("canos_hierro_liv")
    hierro_sp = Base_Datos_Medidas.entradas("canos_hierro_sp")
    gal_liv = Base_Datos_Medidas.entradas("canos_gal_liv")
    gal_pes = Base_Datos_Medidas.entradas("canos_gal_pes")
    return render(request, "canos/canos.html", {"plastico_sp": plastico_sp,
                                                "plastico_ep": plastico_ep,
                                                "plastico_lh": plastico_lh,
                                                "hierro_liv": hierro_liv,
                                                "hierro_sp": hierro_sp,
                                                "gal_liv": gal_liv,
                                                "gal_pes": gal_pes},)
