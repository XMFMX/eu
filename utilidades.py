class Utilidades:
    @staticmethod
    def conversor_pesos_dolares(cantidad, total, tipo_cambio):
        precio_unitario = total / cantidad / tipo_cambio
        return precio_unitario

    @staticmethod
    def conversor_dolares_pesos(cantidad, total, tipo_cambio):
        precio_unitario = total / cantidad * tipo_cambio
        return precio_unitario

    @staticmethod
    def divisor_cantidades(cantidad, total):
        precio_unitario = total / cantidad
        return precio_unitario
