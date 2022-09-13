from CuentaBancaria import CuentaBancaria

# Crear 2 cuentas
cta1 = CuentaBancaria(0.01,10)
cta2 = CuentaBancaria(0.01)

# Cuenta 1: 3 depositos, 1 retiro, intereses, mostrar, metodos encadenados
print("Cuenta 1")
cta1.deposito(10).deposito(20).deposito(50).retiro(70).generar_interés().mostrar_info_cuenta()

# Cuenta 2: 2 depositos, 4 retiros, intereses, mostrar, metodos encadenados
print("Cuenta 2")
cta2.deposito(100).deposito(50).retiro(50).retiro(70).retiro(35).generar_interés().mostrar_info_cuenta()

# BONUS Ninja
"""
utiliza un método de clase para imprimir 
todas las instancias de la información de una cuenta bancaria
"""
CuentaBancaria.imprimir_cuentas()