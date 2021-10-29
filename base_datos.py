import sqlite3
from sqlite3 import Error


class Base_Datos:
    @staticmethod
    def sql_connection():
        try:
            con = sqlite3.connect('base_datos.db')
            return con
        except Error:
            print(Error)

    @staticmethod
    def tabla_conversor_pesos_dolares():
        try:
            con = Base_Datos.sql_connection()
            instruccion = "CREATE TABLE tabla_conversor_pesos_dolares(" \
                          "id integer NOT NULL PRIMARY KEY AUTOINCREMENT, " \
                          "cantidad Integer, " \
                          "total Real, " \
                          "tipo_cambio Real, " \
                          "precio Real)"
            con.execute(instruccion)
            con.commit()
        except Error:
            print(Error)

    @staticmethod
    def tabla_conversor_dolares_pesos():
        try:
            con = Base_Datos.sql_connection()
            instruccion = "CREATE TABLE tabla_conversor_dolares_pesos(" \
                          "id integer NOT NULL PRIMARY KEY AUTOINCREMENT, " \
                          "cantidad Integer, " \
                          "total Real, " \
                          "tipo_cambio Real, " \
                          "precio Real)"
            con.execute(instruccion)
            con.commit()
        except Error:
            print(Error)

    @staticmethod
    def tabla_divisor_cantidades():
        try:
            con = Base_Datos.sql_connection()
            instruccion = "CREATE TABLE tabla_divisor_cantidades(" \
                          "id integer NOT NULL PRIMARY KEY AUTOINCREMENT, " \
                          "cantidad Integer, " \
                          "total Real, " \
                          "precio Real)"
            con.execute(instruccion)
            con.commit()
        except Error:
            print(Error)

    @staticmethod
    def alta_pesos_dolares(cantidad, total, tipo_cambio):
        try:
            con = Base_Datos.sql_connection()
            instruccion = "INSERT INTO tabla_conversor_pesos_dolares(cantidad, total, tipo_cambio, precio)" \
                          "VALUES(?,?,?,?)"
            lista = (cantidad, total, tipo_cambio, float("{:.8f}".format(total / cantidad / tipo_cambio)))
            con.execute(instruccion, lista)
            con.commit()
        except Error:
            print(Error)

    @staticmethod
    def alta_dolares_pesos(cantidad, total, tipo_cambio):
        try:
            con = Base_Datos.sql_connection()
            instruccion = "INSERT INTO tabla_conversor_dolares_pesos(cantidad, total, tipo_cambio, precio)" \
                          "VALUES(?,?,?,?)"
            lista = (cantidad, total, tipo_cambio, float("{:.8f}".format(total / cantidad * tipo_cambio)))
            con.execute(instruccion, lista)
            con.commit()
        except Error:
            print(Error)

    @staticmethod
    def alta_divisor_cantidades(cantidad, total):
        try:
            con = Base_Datos.sql_connection()
            instruccion = "INSERT INTO tabla_divisor_cantidades(cantidad, total, precio) VALUES(?,?,?)"
            lista = (cantidad, total, float("{:.8f}".format(total / cantidad)))
            con.execute(instruccion, lista)
            con.commit()
        except Error:
            print(Error)

    @staticmethod
    def entradas(tabla):
        instruccion = f"SELECT * FROM {tabla}"
        con = Base_Datos.sql_connection()
        cursor = con.cursor()
        cursor.execute(instruccion)
        entradas_tabla = cursor.fetchall()
        return entradas_tabla

    @staticmethod
    def eliminar(tabla, id):
        instruccion = f"DELETE FROM {tabla} WHERE id={id}"
        con = Base_Datos.sql_connection()
        con.execute(instruccion)
        con.commit()


Base_Datos.sql_connection()
Base_Datos.tabla_conversor_pesos_dolares()
Base_Datos.tabla_conversor_dolares_pesos()
Base_Datos.tabla_divisor_cantidades()
