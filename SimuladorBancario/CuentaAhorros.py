class CuentaAhorros:
    #aqui va el codigo

    '''-------------------------------------------------------------------------------------------------------
    # Atributos
    -------------------------------------------------------------------------------------------------------'''

    saldo=0
    interesMensual=0

    '''-------------------------------------------------------------------------------------------------------
    # Metodos
    --------------------------------------------------------------------------------------------------------'''

    def Consignar(self):
        consignar = self.saldo + ">0"
        return "saldo actualizado" + consignar
    
    def ConsultarSaldo(self):
        return self.saldo
    
    def Retirar(self):
        retirar = self.saldo - ">0"
        return "saldo actualizado" + retirar
    
    def ConsultarInteresMensual(self):
        return self.interesMensual