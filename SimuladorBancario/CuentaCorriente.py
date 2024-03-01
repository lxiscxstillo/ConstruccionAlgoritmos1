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
    
    def Consignar(self, Monto):
        consignar = self.saldo + Monto
        return "saldo actualizado" + consignar
    
    def Retirar(self, Monto): 
        retirar = self.saldo - Monto
        return "saldo actualizado" + retirar