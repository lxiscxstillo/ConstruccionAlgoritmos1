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

    def Consignar(self, monto):
        self.saldo += monto
    
    def ConsultarSaldo(self):
        return self.saldo
    
    def Retirar(self, monto): 
        self.saldo -= monto
    
    def ConsultarInteresMensual(self):
        return self.interesMensual