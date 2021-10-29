from django.shortcuts import render
from django.template import RequestContext, loader
from forms import FormularioConductores
from base_datos_medidas import Base_Datos_Medidas


def medidas(request):
    if request.method == "POST":
        formulario_conductores = FormularioConductores(request.POST)
        if formulario_conductores.is_valid():
            diametro = float(formulario_conductores.cleaned_data["conductor"])
            print(diametro)
            plastico_bsc = Base_Datos_Medidas.prensacable("plastico_bsc", diametro)
            plastico_bsp = Base_Datos_Medidas.prensacable("plastico_bsp", diametro)
            plastico_pg = Base_Datos_Medidas.prensacable("plastico_pg", diametro)
            metalico_bsc = Base_Datos_Medidas.prensacable("metalico_bsc", diametro)
            metalico_bsp = Base_Datos_Medidas.prensacable("metalico_bsp", diametro)
            metalico_pc = Base_Datos_Medidas.prensacable("metalico_pc", diametro)

    formulario_conductores = FormularioConductores()

    try:
        plastico_bsc = Base_Datos_Medidas.prensacable("plastico_bsc", diametro)
        plastico_bsp = Base_Datos_Medidas.prensacable("plastico_bsp", diametro)
        plastico_pg = Base_Datos_Medidas.prensacable("plastico_pg", diametro)
        metalico_bsc = Base_Datos_Medidas.prensacable("metalico_bsc", diametro)
        metalico_bsp = Base_Datos_Medidas.prensacable("metalico_bsp", diametro)
        metalico_pc = Base_Datos_Medidas.prensacable("metalico_pc", diametro)
    except UnboundLocalError:
        plastico_bsc = []
        plastico_bsp = []
        plastico_pg = []
        metalico_bsc = []
        metalico_bsp = []
        metalico_pc = []

    return render(request, "medidas/medidas.html",
                  {"formulario_conductores": formulario_conductores,
                   "plastico_bsc": plastico_bsc,
                   "plastico_bsp": plastico_bsp,
                   "plastico_pg": plastico_pg,
                   "metalico_bsc": metalico_bsc,
                   "metalico_bsp": metalico_bsp,
                   "metalico_pc": metalico_pc}
                  )
