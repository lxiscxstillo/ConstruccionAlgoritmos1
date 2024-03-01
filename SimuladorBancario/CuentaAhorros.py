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

    def Consignar(self, Monto):
        consignar = self.saldo + Monto
        return "saldo actualizado" + consignar
    
    def ConsultarSaldo(self):
        return self.saldo
    
    def Retirar(self, Monto): 
        retirar = self.saldo - Monto
        return "saldo actualizado" + retirar
    
    def ConsultarInteresMensual(self):
        return self.interesMensual