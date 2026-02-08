import datetime
import random
class CuentaBancaria:
    """Clase bancaria mínima con todos tus parámetros"""
    
    def  __init__(self, cliente, saldo=0):
        self.nombre_cliente = cliente
        self.numero_cuenta = f"CT-{random.randint(100000, 999999)}"
        self.fecha_apertura = datetime.datetime.now()
        self.balance = saldo
    
    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            return True
        return False
    
    def retirar(self, monto):
        if 0 < monto <= self.balance:
            self.balance -= monto
            return True
        return False
    
    def consultar(self):
        return self.balance

# Ejemplo de uso instantáneo
if __name__:str == "__main__"
    # Crear cuenta
mi_cuenta = CuentaBancaria("Juan Pérez", 1000)
    
    # Acceder a TODOS tus parámetros
print(f"Cliente: {mi_cuenta.nombre_cliente}")
print(f"Cuenta: {mi_cuenta.numero_cuenta}")
print(f"Apertura: {mi_cuenta.fecha_apertura}")
print(f"Balance: ${mi_cuenta.balance}")
    
    # Usar tus métodos solicitados
mi_cuenta.depositar(500)
mi_cuenta.retirar(300)
print(f"Nuevo balance: ${mi_cuenta.consultar()}")