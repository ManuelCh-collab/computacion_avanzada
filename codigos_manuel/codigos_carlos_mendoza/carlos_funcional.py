import datetime

class CuentaBancaria:
    def __init__(self, numero_cuenta, nombre_cliente, balance_inicial=0.0):
        self.numero_cuenta = numero_cuenta
        self.nombre_cliente = nombre_cliente
        self.balance = float(balance_inicial)
        self.fecha_apertura = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        # Mensaje de bienvenida humano al crear la cuenta
        print(f"\n ¡Bienvenido a Industrias Mendoza, {self.nombre_cliente}!")
        print(f"   Su cuenta {self.numero_cuenta} está lista para operar.")

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print(f" [Industrias Mendoza] Hemos recibido su depósito de ${monto:.2f}. ¡Gracias por confiar en nosotros! (Saldo actual: ${self.balance:.2f})")
        else:
            print(" Ups, el monto a depositar debe ser mayor a cero.")

    def retirar(self, monto):
        if monto > 0:
            if self.balance >= monto:
                self.balance -= monto
                print(f" [Industrias Mendoza] Retiro de ${monto:.2f} procesado con éxito. Que tenga un excelente día. (Saldo restante: ${self.balance:.2f})")
            else:
                print(f" Estimado cliente, sus fondos en Industrias Mendoza son insuficientes para este retiro. (Saldo disponible: ${self.balance:.2f})")
        else:
            print(" El monto a retirar debe ser válido.")

    def mostrar_informacion(self):
        print(f"\n---  ESTADO DE CUENTA: INDUSTRIAS MENDOZA ---")
        print(f" Cliente: {self.nombre_cliente} |  Cuenta: {self.numero_cuenta}")
        print(f" Desde:   {self.fecha_apertura}")
        print(f" Balance: ${self.balance:.2f}")
        print("-----------------------------------------------\n")

# --- PRUEBA RÁPIDA ---
if __name__== "__main__":
    cta = CuentaBancaria("IM-9988", "Carlos Mendoza", 1000)
    cta.depositar(500)
    cta.retirar(200)
    cta.retirar(5000) # Intento fallido para ver el mensaje amable
    cta.mostrar_informacion()