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
    
    def Consignar(self):
        consignar = self.saldo + ">0"
        return "saldo actualizado" + consignar
    
    def Retirar(self):
        retirar = self.saldo - ">0"
        return "saldo actualizado" + retirar