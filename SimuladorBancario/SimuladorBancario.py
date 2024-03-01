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
    CDT = CDT()
    CuentaAhorros = CuentaAhorros()
    CuentaCorriente = CuentaCorriente()

    '''
    # Metodos
    '''

    def ConsignarCuentaCorriente(self):
        return self.CuentaCorriente.Consignar()
    
    def ConsultarSaldoTotal(self):
        saldoTotal = self.CuentaCorriente.ConsultarSaldo() + self.CuentaAhorros.ConsultarSaldo()
        return saldoTotal
    
    def TransferirAhorrosCorriente(self, monto):
        return 