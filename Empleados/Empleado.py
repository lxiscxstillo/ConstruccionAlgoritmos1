from Fecha import Fecha

class Empleado:
    #aqui va el codigo

    '''--------------------------------------------------------
    # Atributos
    ---------------------------------------------------------'''

    nombre=''
    apellido=''
    '''---------------------------------------------------------
    # 1 = Masculino y 2 = Femenino
    ----------------------------------------------------------'''
    sexo=0
    salario=0
    numero_hijos_empleado=0

    '''----------------------------------------------------------
    # Asociaciones
    ----------------------------------------------------------'''
    fechaNacimiento = Fecha()
    fechaIngreso = Fecha()

    '''----------------------------------------------------------
    # Metodos
    -----------------------------------------------------------'''

    # constructor

    def __init__(self, nombres, apellidos, salario, sexo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.salario = salario
        self.sexo = sexo

    def ConsultarHijosEmpleado(self):
        return "El numero de hijos del empleado es " + self.numero_hijos_empleado
    
    def CalcularAuxilioEducativo(self):
        "el total del auxilio educativo para el empleado es de " + (self.ConsultarSalario * 0.05) * self.ConsultarHijosEmpleado

    def CalcularAuxilioEducativoEmpleado(self, porcentajeSalario):
        "el total del auxilio educativo para el empleado es de" + self.ConsultarSalario * porcentajeSalario

    def CalcularDiferenciaSalarialRespectoOtroEmpleado(self, salarioSegundoEmpleado):
        # salarioSegundoEmpleado = Empleado.ConsultarSalario
        return self.ConsultarSalario - salarioSegundoEmpleado


    def CambiarSalario(self, nSalario):
        #aqui va el codigo
        self.salario=nSalario
        return "Su nuevo salario es " + self.salario
    
    def ConsultarSalario(self):
        #aqui va el codigo
        return self.salario
    
    def AumentoSalario(self):
        #aqui va el codigo
        aumento = self.salario*0.05
        nSalario = self.salario+aumento
        self.salario = nSalario
        return "Su nuevo salario es " + self.salario
    
    def DuplicarSalario(self):
        #forma 1
        nuevoSalario = self.salario*2
        self.salario = nuevoSalario

        # #forma 2
        # self.salario *= 2

    def CalcularSalarioAnual(self):
        #forma 1
        salarioAnual = self.salario*12
        return salarioAnual
    
        # #forma 2
        # return self.salario*12
    
    def ConsultarCumpleanios(self):
        return self.fechaNacimiento.ConsultarDia()
    
    def ConsultarIVA(self):
        impuesto = self.CalcularSalarioAnual() * 0.195
        return impuesto 
    
# Empleado.__init__(Empleado,'pepe', 'perez', 1000, 1)
# Empleado.ConsultarHijosEmpleado(Empleado) 