class Bancanimo:

    def __init__(self, numero_cuenta, nombre_cliente, fecha_apertura, banlance=100000.0):
        self.numero_cuenta = numero_cuenta
        self.nombre_cliente = nombre_cliente
        self.fecha_apertura = fecha_apertura
        self.balance = banlance
        
        
    def pago(self, monto):
        if 0 < monto <= self.balance: 
            self.balance == monto 
            print(f"pago realizado: {monto}, Balance actual: {self.balance}")
            
        else:
            print(f"saldo insuficiente o monto invalido")
            
    def retiro(self, monto):
        if 0 < monto <= self.balance:
            self.balance -= monto
            print(f"retiro exitoso: {monto}, Balance actual: {self.balance}")
        
        else:
            print("Fondos insuficiente intentelo mas tarde")
            
    def mostrar_balance(self):
        
        print(f"Balance disponible: {self.balance}")
        
# ejemplo
cuenta1 = Bancanimo("123456789", "Manuel Chirivella","date(2025, 12, 22), 15000.0)")
print("Cliente: Manuel chirivella")
cuenta1.mostrar_balance()
cuenta1.pago(600)     # Pago de un servicio
cuenta1.retiro(300)   # Retiro en efectivo
cuenta1.mostrar_balance() # Balance
