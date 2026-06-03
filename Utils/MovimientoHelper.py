class MovimientoHelper:

    @staticmethod
    def calcular_discrepancia(peso_salida, peso_llegada):
        return round(peso_salida - peso_llegada, 2)

    @staticmethod
    def tiene_discrepancia(peso_salida, peso_llegada):
        return peso_salida != peso_llegada

    @staticmethod
    def obtener_estado_discrepancia(peso_salida, peso_llegada):

        diferencia = peso_salida - peso_llegada

        if diferencia > 0:
            return f"Pérdida de {diferencia:.2f} toneladas"

        if diferencia < 0:
            return f"Exceso de {abs(diferencia):.2f} toneladas"

        return "Sin discrepancia"