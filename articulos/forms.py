from django import forms
from .models import TSM
import json


def leerjson(archivo):
    with open(archivo, 'r') as fp:
        return json.load(fp)


def conseguir_tipo():
    """ GET COUNTRY SELECTION """
    archivo = './base_articulos.json'
    datos = leerjson(archivo)
    tipos = [('-----', '---Tipo---')]
    for x in datos:
        y = (x['tipo'], x['tipo'])
        tipos.append(y)
    return tipos


def subtipo_por_tipo(tipo):
    """ GET STATE SELECTION BY COUNTRY INPUT """
    archivo = './base_articulos.json'
    datos = leerjson(archivo)
    subtipos = []
    for x in datos:
        if x['tipo'] == tipo:
            if 'subtipo' in x:
                for subtipo in x['subtipo']:
                    y = (subtipo['subtipo'], subtipo['subtipo'])
                    subtipos.append(subtipo['subtipo'])
            else:
                subtipos.append(tipo)
    return subtipos


class FormularioSubtipo(forms.ModelForm):
    tipo = forms.ChoiceField(
        choices=conseguir_tipo(),
        required=False,
        label='Tipo de Articulo',
        widget=forms.Select(attrs={'class': 'form-control', 'tipo': 'tipo'}),
    )

    class Meta:
        model = TSM
        fields = ['tipo']
