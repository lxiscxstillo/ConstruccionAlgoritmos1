class CuentaCorriente:
    #Aqui va el codigo

    '''-----------------------------------------------------------------------------------------------------
    # Atributos
    -----------------------------------------------------------------------------------------------------'''

    saldo=0

    '''-----------------------------------------------------------------------------------------------------
    # Metodos
    -----------------------------------------------------------------------------------------------------'''

    def ConsultarSaldo(self):
        return self.saldo
    
    def Consignar(self, monto):
        self.saldo += monto
    
    def Retirar(self, monto): 
        descuento = monto * 0.01
        self.saldo -= monto + descuento