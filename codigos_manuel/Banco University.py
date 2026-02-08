import random
import json
from datetime import date

class Banco_University:
    def __init__(self, nombre_cliente: str, fecha_apertura: str, balance_inicial: float = 0.0, numero_cuenta: str = None) -> None:
        
        self.numero_cuenta: str = numero_cuenta if numero_cuenta else str(random.randint(100000, 999999))
        self.nombre_cliente: str = nombre_cliente
        self.fecha_apertura: str = fecha_apertura
        self.balance: float = balance_inicial

    def mostrar_info(self) -> None:
        print("\n=== Información de la cuenta ===")
        print(f"Cliente: {self.nombre_cliente}")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Fecha de apertura: {self.fecha_apertura}")
        print(f"Balance actual: Bs{self.balance:.2f}")

    def pago(self, monto: float) -> None:
        if monto > 0:
            self.balance += monto
            print(f"Pago realizado: +Bs{monto:.2f}")
        else:
            print("El monto debe ser positivo.")

    def retiro(self, monto: float) -> None:
        if monto <= 0:
            print("El monto debe ser positivo.")
        elif monto > self.balance:
            print("Fondos insuficientes.")
        else:
            self.balance -= monto
            print(f"Retiro realizado: -Bs{monto:.2f}")

    def mostrar_balance(self) -> None:
        print(f"Balance actualizado: Bs{self.balance:.2f}")

    def to_dict(self) -> dict:
        return {
            "numero_cuenta": self.numero_cuenta,
            "nombre_cliente": self.nombre_cliente,
            "fecha_apertura": self.fecha_apertura,
            "balance": self.balance
        }



def cargar_cuentas() -> dict:
    try:
        with open("cuentas.json", "r") as f:
            data = json.load(f)
            return {c["numero_cuenta"]: Banco_University(c["nombre_cliente"], c["fecha_apertura"], c["balance"], c["numero_cuenta"]) for c in data}
    except FileNotFoundError:
        return {}

def guardar_cuentas(cuentas: dict) -> None:
    data = [cuenta.to_dict() for cuenta in cuentas.values()]
    with open("cuentas.json", "w") as f:
        json.dump(data, f, indent=4)



cuentas = cargar_cuentas()

def crear_cuenta() -> None:
    nombre_cliente = input("Ingrese nombre del cliente: ")
    balance_inicial = float(input("Ingrese balance inicial: "))
    nueva_cuenta = Banco_University(nombre_cliente, str(date.today()), balance_inicial)
    cuentas[nueva_cuenta.numero_cuenta] = nueva_cuenta
    guardar_cuentas(cuentas)
    print("\nCuenta creada exitosamente.")
    nueva_cuenta.mostrar_info()

def ingresar_cuenta() -> None:
    numero = input("Ingrese el número de cuenta: ")
    if numero in cuentas:
        cuenta = cuentas[numero]
        print(f"\nIngresando a la cuenta de {cuenta.nombre_cliente}...")
        cuenta.mostrar_info()

        while True:
            print("\n--- Menú de operaciones ---")
            print("1. Pago (depositar dinero)")
            print("2. Retiro (sacar dinero)")
            print("3. Mostrar balance")
            print("4. Salir de esta cuenta")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                monto = float(input("Ingrese monto a depositar: "))
                cuenta.pago(monto)
                guardar_cuentas(cuentas)
            elif opcion == "2":
                monto = float(input("Ingrese monto a retirar: "))
                cuenta.retiro(monto)
                guardar_cuentas(cuentas)
            elif opcion == "3":
                cuenta.mostrar_balance()
            elif opcion == "4":
                print("Saliendo de la cuenta...")
                break
            else:
                print("Opción inválida.")
    else:
        print("No existe una cuenta con ese número.")


while True:
    print("\n=== Sistema Bancario ===")
    print("1. Crear nueva cuenta")
    print("2. Ingresar a una cuenta existente")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_cuenta()
    elif opcion == "2":
        ingresar_cuenta()
    elif opcion == "3":
        print("Saliendo del sistema bancario...")
        break
    else:
        print("Opción inválida.")