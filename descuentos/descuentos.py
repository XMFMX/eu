class Descuentos():
    @staticmethod
    def convertir_porcentaje_descuento(valor):
        porcentaje = 1 - (valor / 100)
        return porcentaje

    @staticmethod
    def convertir_porcentaje_rentabilidad(valor):
        porcentaje = 1 + (valor / 100)
        return porcentaje

    @staticmethod
    def precio(costo, d0=1, d1=1, d2=1, d3=1, d4=1, d5=1, d6=1, d7=1, d8=1, d9=1, rent=1.3, **kwargs):
        desc0 = Descuentos.convertir_porcentaje_descuento(d0)
        desc1 = Descuentos.convertir_porcentaje_descuento(d1)
        desc2 = Descuentos.convertir_porcentaje_descuento(d2)
        desc3 = Descuentos.convertir_porcentaje_descuento(d3)
        desc4 = Descuentos.convertir_porcentaje_descuento(d4)
        desc5 = Descuentos.convertir_porcentaje_descuento(d5)
        desc6 = Descuentos.convertir_porcentaje_descuento(d6)
        desc7 = Descuentos.convertir_porcentaje_descuento(d7)
        desc8 = Descuentos.convertir_porcentaje_descuento(d8)
        desc9 = Descuentos.convertir_porcentaje_descuento(d9)
        rent = Descuentos.convertir_porcentaje_rentabilidad(rent)
        precio = costo * desc0 * desc1 * desc2 * desc3 * desc4 * desc5 * desc6 * desc7 * desc8 * desc9 * rent
        return precio
