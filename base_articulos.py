import sqlite3
from sqlite3 import Error
import shelve
import json


class BaseArticulos:
    @staticmethod
    def sql_connection():
        try:
            con = sqlite3.connect('base_articulos.db')
            return con
        except Error:
            print(Error)

    @staticmethod
    def entradas(columna):
        instruccion = f"SELECT * FROM articulos ORDER BY {columna}"
        con = BaseArticulos.sql_connection()
        cursor = con.cursor()
        cursor.execute(instruccion)
        entradas_tabla = cursor.fetchall()
        return entradas_tabla

    @staticmethod
    def tabla_tipo():
        try:
            con = BaseArticulos.sql_connection()
            instruccion = "CREATE TABLE tabla_tipo(tipo Text)"
            con.execute(instruccion)
            con.commit()
        except Error:
            print(Error)

    @staticmethod
    def tabla_subtipo():
        try:
            con = BaseArticulos.sql_connection()
            instruccion = "CREATE TABLE tabla_subtipo(subtipo Text)"
            con.execute(instruccion)
            con.commit()
        except Error:
            print(Error)

    @staticmethod
    def tabla_marca():
        try:
            con = BaseArticulos.sql_connection()
            instruccion = "CREATE TABLE tabla_marca(marca Text)"
            con.execute(instruccion)
            con.commit()
        except Error:
            print(Error)

    @staticmethod
    def alta(tabla, columna, valor):
        try:
            con = BaseArticulos.sql_connection()
            instruccion = f"INSERT INTO {tabla}({columna})" \
                          "VALUES(?)"
            lista = (valor)
            con.execute(instruccion, lista)
            con.commit()
        except Error:
            print(Error)

    @staticmethod
    def completar_tablas():
        BaseArticulos.tabla_tipo()
        BaseArticulos.tabla_subtipo()
        BaseArticulos.tabla_marca()
        tipo_articulo = {}
        subtipo_articulo = {}
        marca_articulo = {}
        datos_tipo = BaseArticulos.entradas("tipo")
        datos_subtipo = BaseArticulos.entradas("subtipo")
        datos_marca = BaseArticulos.entradas("marca")
        for x in datos_tipo:
            tipo_articulo.update({x[1]: str(x[1])})
        for x in datos_subtipo:
            subtipo_articulo.update({x[2]: str(x[2])})
        for x in datos_marca:
            marca_articulo.update({x[3]: str(x[3])})

        for x in tipo_articulo:
            valor = (tipo_articulo[x],)
            BaseArticulos.alta("tabla_tipo", "tipo", valor)
            print(valor[0])
        for x in subtipo_articulo:
            valor = (subtipo_articulo[x],)
            BaseArticulos.alta("tabla_subtipo", "subtipo", valor)
            print(valor[0])
        for x in marca_articulo:
            valor = (marca_articulo[x],)
            BaseArticulos.alta("tabla_marca", "marca", valor)
            print(valor[0])

    @staticmethod
    def tabla_tipo_subtipo_marca():
        try:
            con = BaseArticulos.sql_connection()
            instruccion = "CREATE TABLE tabla_tipo_subtipo_marca(" \
                          "tipo TEXT, " \
                          "subtipos TEXT, " \
                          "marcas TEXT)"
            con.execute(instruccion)
            con.commit()
        except Error:
            print(Error)

    @staticmethod
    def tipo_subtipo_marca():
        tsm = shelve.open("tipo_subtipo_marca")
        BaseArticulos.tabla_tipo_subtipo_marca()
        tipo = BaseArticulos.entradas_tipo()
        tipo_subtipo_marca = {}
        for x in tipo:
            subtipo = {}
            marca = {}
            ls = []
            lm = []
            for y in BaseArticulos.entradas_tipo_subtipo_marca("subtipo", x[0]):
                subtipo.update({y: y[0]})
            for y in BaseArticulos.entradas_tipo_subtipo_marca("marca", x[0]):
                marca.update({y: y[0]})
            for z in subtipo:
                ls.append(subtipo[z])
            for z in marca:
                lm.append(marca[z])
            tipo_subtipo_marca.update({x[0]: (ls, lm)})
        tsm.update(tipo_subtipo_marca)
        tsm.sync()
        tsm.close()
        return tipo_subtipo_marca

    @staticmethod
    def alta_tipo_subtipo_marca():
        tipo_subtipo_marca = BaseArticulos.tipo_subtipo_marca()
        for x in tipo_subtipo_marca:
            print(x)
            print(tipo_subtipo_marca[x][0])
            print(tipo_subtipo_marca[x][1])
            try:
                con = BaseArticulos.sql_connection()
                instruccion = f"INSERT INTO tabla_tipo_subtipo_marca(tipo, subtipos, marcas)" \
                              "VALUES(?,?,?)"
                lista = (str(x), str(tipo_subtipo_marca[x][0]), str(tipo_subtipo_marca[x][1]))
                con.execute(instruccion, lista)
                con.commit()
            except Error:
                print(Error)

    @staticmethod
    def entradas_tipo_subtipo_marca(columna, tipo):
        instruccion = f"SELECT {columna} FROM articulos WHERE tipo='{tipo}' ORDER BY {columna}"
        con = BaseArticulos.sql_connection()
        cursor = con.cursor()
        cursor.execute(instruccion)
        entradas_tabla = cursor.fetchall()
        return entradas_tabla

    @staticmethod
    def entradas_tipo():
        instruccion = f"SELECT * FROM tabla_tipo ORDER BY tipo"
        con = BaseArticulos.sql_connection()
        cursor = con.cursor()
        cursor.execute(instruccion)
        entradas_tabla = cursor.fetchall()
        return entradas_tabla

    @staticmethod
    def crear_json():
        bd_json = open("base_articulos.json", "a")
        c = BaseArticulos.tsm_items
        bd_json.write("[\n")
        for x in c:
            subtipo = {}
            marca = {}
            for y in x[1][0]:
                subtipo.update({y: y})
            for y in x[1][1]:
                marca.update({y: y})
            bd_json.write("    {\n")
            bd_json.write(f'        "tipo": "{x[0]}",\n        "subtipo": { subtipo },\n        "marca": { marca }')
            bd_json.write("\n    },\n")
        bd_json.write("]")
        bd_json.close()

    tsm = shelve.open("tipo_subtipo_marca")
    tsm_tipo = list(tsm.keys())
    tsm_subtipo_marca = list(tsm.values())
    tsm_items = list(tsm.items())
    tsm.close()


# BaseArticulos.tipo_subtipo_marca()
a = BaseArticulos.tsm_tipo
b = BaseArticulos.tsm_subtipo_marca
c = BaseArticulos.tsm_items
for x in c:
    print(x)
    print(x[0])
    print(x[1][0])
    print(x[1][1])
"""for x in b:
    print(x[0], x[1])"""
# BaseArticulos.crear_json()
