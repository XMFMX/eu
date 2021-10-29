import sqlite3
from sqlite3 import Error


class Base_Datos_Medidas:
    @staticmethod
    def sql_connection():
        try:
            con = sqlite3.connect('medidas.db')
            return con
        except Error:
            print(Error)

    @staticmethod
    def tabla_calculo_prensacable():
        try:
            con = Base_Datos_Medidas.sql_connection()
            instruccion = "CREATE TABLE tabla_calculo_prensacable(medida Real)"
            con.execute(instruccion)
            con.commit()
        except Error:
            print(Error)

    @staticmethod
    def alta_calculo_prensacable(medida):
        try:
            con = Base_Datos_Medidas.sql_connection()
            instruccion = "INSERT INTO tabla_calculo_prensacable(medida)" \
                          "VALUES(?)"
            lista = [float(medida)]
            con.execute(instruccion, lista)
            con.commit()
        except Error:
            print(Error)

    @staticmethod
    def eliminar():
        instruccion = f"DELETE FROM tabla_calculo_prensacable"
        con = Base_Datos_Medidas.sql_connection()
        con.execute(instruccion)
        con.commit()

    @staticmethod
    def entradas(tabla):
        instruccion = f"SELECT * FROM {tabla}"
        con = Base_Datos_Medidas.sql_connection()
        cursor = con.cursor()
        cursor.execute(instruccion)
        entradas_tabla = cursor.fetchall()
        return entradas_tabla

    @staticmethod
    def prensacable(tabla, medida):
        instruccion = f"SELECT * FROM {tabla}"
        con = Base_Datos_Medidas.sql_connection()
        cursor = con.cursor()
        cursor.execute(instruccion)
        entradas = cursor.fetchall()
        lista = []
        for x in entradas:
            if x[3] <= medida <= x[4]:
                lista.append(x)
            else:
                pass
        return lista
