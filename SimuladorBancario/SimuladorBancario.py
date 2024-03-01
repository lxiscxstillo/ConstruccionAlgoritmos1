from CuentaCorriente import CuentaCorriente
from CuentaAhorros import CuentaAhorros
from CDT import CDT

class SimuladorBancario:
    #Aqui va el codigo
    '''
    Atributos
    '''
    cedula=0
    nombres=0
    mes_actual=0

    '''
    # Asociaciones
    '''
    cdt = CDT()
    ahorros = CuentaAhorros()
    corriente = CuentaCorriente()

    '''
    # Metodos
    '''

    def ConsignarCuentaCorriente(self, monto):
        self.corriente.Consignar(monto)
    
    def ConsignarCuentaAhorros(self, monto):
        self.ahorros.Consignar(monto)
    
    def ConsultarSaldoTotal(self):
        return self.corriente.ConsultarSaldo() + self.ahorros.ConsultarSaldo()
    
    def TransferirAhorrosACorriente(self):
        self.ConsignarCuentaCorriente(self.ahorros.ConsultarSaldo)
        self.ahorros.Retirar(self.ahorros.ConsultarSaldo)
    
    def RetirarCuentaAhorros(self, monto):
        self.ahorros.Retirar(monto)

    def RetirarCuentaCorriente(self, monto):
        self.ahorros.Retirar(monto)
        
    def ConsultarSaldoCuentaCorriente(self):
        return self.corriente.ConsultarSaldo()
    
    def RetirarTodo(self):
        total = self.ConsultarSaldoTotal()
        self.TransferirAhorrosACorriente()
        self.RetirarCuentaCorriente

        return total
    
    def DuplicarAhorro(self):
        self.ConsignarCuentaAhorros(self.ahorros.ConsultarSaldo)