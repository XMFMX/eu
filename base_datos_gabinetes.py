import sqlite3
from sqlite3 import Error


class Base_Datos_Gabinete:
    @staticmethod
    def sql_connection():
        try:
            con = sqlite3.connect('genrod_gabexel.db')
            return con
        except Error:
            print(Error)

    @staticmethod
    def tabla_gabinete_genrod():
        try:
            con = Base_Datos_Gabinete.sql_connection()
            instruccion = "CREATE TABLE tabla_gabinete_genrod(" \
                          "id integer NOT NULL PRIMARY KEY AUTOINCREMENT, " \
                          "codigo_eu Integer)"
            con.execute(instruccion)
            con.commit()
        except Error:
            print(Error)

    @staticmethod
    def tabla_gabinete_gabexel():
        try:
            con = Base_Datos_Gabinete.sql_connection()
            instruccion = "CREATE TABLE tabla_gabinete_gabexel(" \
                          "id integer NOT NULL PRIMARY KEY AUTOINCREMENT, " \
                          "codigo_eu Integer)"
            con.execute(instruccion)
            con.commit()
        except Error:
            print(Error)

    @staticmethod
    def alta_gabinete(tabla, codigo):
        try:
            con = Base_Datos_Gabinete.sql_connection()
            instruccion = f"INSERT INTO {tabla}(codigo_eu)" \
                          "VALUES(?)"
            lista = (codigo,)
            con.execute(instruccion, lista)
            con.commit()
        except Error:
            print(Error)

    @staticmethod
    def entradas_gabinetes_genrod():
        instruccion = f"SELECT codigo_eu FROM tabla_gabinete_genrod"
        con = Base_Datos_Gabinete.sql_connection()
        cursor = con.cursor()
        cursor.execute(instruccion)
        entradas_tabla = cursor.fetchall()
        return entradas_tabla

    @staticmethod
    def entradas_gabinetes_gabexel():
        instruccion = f"SELECT codigo_eu FROM tabla_gabinete_gabexel"
        con = Base_Datos_Gabinete.sql_connection()
        cursor = con.cursor()
        cursor.execute(instruccion)
        entradas_tabla = cursor.fetchall()
        return entradas_tabla

    @staticmethod
    def entradas_genrod_calado_abisagrado(codigo_eu):
        instruccion = f"SELECT * FROM genrod_calado_abisagrado WHERE codigo_eu_gabinete={codigo_eu}"
        con = Base_Datos_Gabinete.sql_connection()
        cursor = con.cursor()
        cursor.execute(instruccion)
        entradas_tabla = cursor.fetchall()
        return entradas_tabla

    @staticmethod
    def entradas_genrod_ciego_abisagrado(codigo_eu):
        instruccion = f"SELECT * FROM genrod_ciego_abisagrado WHERE codigo_eu_gabinete={codigo_eu}"
        con = Base_Datos_Gabinete.sql_connection()
        cursor = con.cursor()
        cursor.execute(instruccion)
        entradas_tabla = cursor.fetchall()
        return entradas_tabla

    @staticmethod
    def entradas_genrod_ciego_fijo(codigo_eu):
        instruccion = f"SELECT * FROM genrod_ciego_fijo WHERE codigo_eu_gabinete={codigo_eu}"
        con = Base_Datos_Gabinete.sql_connection()
        cursor = con.cursor()
        cursor.execute(instruccion)
        entradas_tabla = cursor.fetchall()
        return entradas_tabla

    @staticmethod
    def entradas_gabexel(codigo_eu):
        instruccion = f"SELECT * FROM gabexel WHERE codigo_eu_gabinete={codigo_eu}"
        con = Base_Datos_Gabinete.sql_connection()
        cursor = con.cursor()
        cursor.execute(instruccion)
        entradas_tabla = cursor.fetchall()
        return entradas_tabla

    @staticmethod
    def eliminar(tabla, id):
        instruccion = f"DELETE FROM {tabla} WHERE codigo_eu={id}"
        con = Base_Datos_Gabinete.sql_connection()
        con.execute(instruccion)
        con.commit()


Base_Datos_Gabinete.tabla_gabinete_genrod()
Base_Datos_Gabinete.tabla_gabinete_gabexel()
