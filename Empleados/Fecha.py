class Fecha:
    #aqui va el codigo

    '''--------------------------------------------------------------------------------------------
    # Atributos
    -----------------------------------------------------------------------------------------------'''

    dia=0
    mes=0
    anio=0

    '''-------------------------------------------------------------------------------------------
    # Metodos
    --------------------------------------------------------------------------------------------'''

    # constructor

    def __init__(self, dia=0, mes=0, anio=0):
        self.dia = dia
        self.mes = mes
        self.anio = anio


    def ConsultarDia(self):
        return self.dia
    
    def ConsultarMes(self):
        return self.mes
    
    def ConsultarAnio(self):
        return self.anio