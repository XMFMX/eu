from django import forms
from django.core.validators import RegexValidator
from base_articulos import BaseArticulos
from articulos.models import TSM
import json

patron_numerico = r"^[0-9.,]*$"

error_cantidad = "Ingrese una Cantidad válida.\nSolo caracteres numéricos."
error_valor = "Ingrese un Valor válido.\nSolo caracteres numéricos, sin símbolos."

regex_cantidad = RegexValidator(patron_numerico, error_cantidad)
regex_valor = RegexValidator(patron_numerico, error_valor)

tsm_tipo = BaseArticulos.tsm_tipo
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


class FormularioConversorPesosDolares(forms.Form):
    cantidad_pd = forms.CharField(label="Cantidad", max_length=20, validators=[regex_cantidad])
    total_pd = forms.CharField(label="Total", max_length=20, validators=[regex_valor])
    tipo_cambio_pd = forms.CharField(label="Tipo de cambio", max_length=20, validators=[regex_valor])


class FormularioConversorDolaresPesos(forms.Form):
    cantidad_dp = forms.CharField(label="Cantidad", max_length=20, validators=[regex_cantidad])
    total_dp = forms.CharField(label="Total", max_length=20, validators=[regex_valor])
    tipo_cambio_dp = forms.CharField(label="Tipo de cambio", max_length=20, validators=[regex_valor])


class FormularioDivisorCantidades(forms.Form):
    cantidad_dc = forms.CharField(label="Cantidad", max_length=20, validators=[regex_cantidad])
    total_dc = forms.CharField(label="Total", max_length=20, validators=[regex_valor])


class FormularioGabinete(forms.Form):
    codigo_gabinete = forms.CharField(label="Codigo EU", max_length=20, validators=[regex_cantidad])


class FormularioConductores(forms.Form):
    conductor = forms.CharField(label="Diametro del Conductor", max_length=20, validators=[regex_valor])


class FormularioDescuentos(forms.Form):
    costo = forms.CharField(label="Costo", max_length=20, validators=[regex_valor], initial=0)
    renta = forms.CharField(label="Rentabilidad", max_length=20, validators=[regex_valor], initial=30)
    desc0 = forms.CharField(label="Descuento 1", max_length=20, validators=[regex_valor], required=False, initial=0)
    desc1 = forms.CharField(label="Descuento 2", max_length=20, validators=[regex_valor], required=False, initial=0)
    desc2 = forms.CharField(label="Descuento 3", max_length=20, validators=[regex_valor], required=False, initial=0)
    desc3 = forms.CharField(label="Descuento 4", max_length=20, validators=[regex_valor], required=False, initial=0)
    desc4 = forms.CharField(label="Descuento 5", max_length=20, validators=[regex_valor], required=False, initial=0)
    desc5 = forms.CharField(label="Descuento 6", max_length=20, validators=[regex_valor], required=False, initial=0)
    desc6 = forms.CharField(label="Descuento 7", max_length=20, validators=[regex_valor], required=False, initial=0)
    desc7 = forms.CharField(label="Descuento 8", max_length=20, validators=[regex_valor], required=False, initial=0)
    desc8 = forms.CharField(label="Descuento 9", max_length=20, validators=[regex_valor], required=False, initial=0)
    desc9 = forms.CharField(label="Descuento 10", max_length=20, validators=[regex_valor], required=False, initial=0)


class FormularioArticulos(forms.Form):
    tipo = forms.CharField(label="Tipo de Articulo", widget=forms.Select(tipo_articulo))
    subtipo = forms.CharField(label="Subtipo de Articulo", widget=forms.Select(subtipo_articulo))
    marca = forms.CharField(label="Marca", widget=forms.Select(marca_articulo))
