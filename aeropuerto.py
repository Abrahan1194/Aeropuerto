# Sistema de Gestion y Costeo de Equipaje Aereo con colores ANSI y menu atractivo

# Diccionario con las rutas disponibles
rutas = {
    "Bogota -> Medellin": {"tipo": "nacional", "precio_base": 230000},
    "Bogota -> Espana": {"tipo": "internacional", "precio_base": 4200000},
}

# Costos adicionales por peso de equipaje principal
costos_equipaje = {
    (0, 20): 50000,
    (21, 30): 70000,
    (31, 50): 110000,
}

# Diccionario para almacenar las reservas
reservas = {}

# Funcion para generar un ID unico para cada reserva
def generar_id():
    return f"COMP{len(reservas) + 1:04}"

# Funcion para registrar una nueva reserva
def registrar_reserva():
    print("\033[34m\nREGISTRO DE RESERVA \033[0m")

    nombre = input("Ingrese el nombre del pasajero: ")
    tipo_viaje = input("Ingrese el tipo de viaje (nacional/internacional): ").lower()

    # Validar tipo de viaje
    if tipo_viaje not in ["nacional", "internacional"]:
        print("\033[91mTipo de viaje no valido\033[0m")
        return

    destino = input("Ingrese el destino (Bogota -> Medellin/Bogota -> Espana): ")

    # Validar destino
    if destino not in rutas:
        print("\033[91mDestino no valido\033[0m")
        return

    peso_equipaje_principal = float(input("Ingrese el peso del equipaje principal (kg): "))

    # Validar peso del equipaje principal
    if peso_equipaje_principal > 50:
        print("\033[91mEquipaje principal no admitido por exceder el limite de peso\033[0m")
        return

    equipaje_mano = input("Lleva equipaje de mano? (si/no): ").lower()

    # Validar equipaje de mano
    if equipaje_mano == "si":
        peso_equipaje_mano = float(input("Ingrese el peso del equipaje de mano (kg): "))
        if peso_equipaje_mano > 13:
            print("\033[93mEquipaje de mano rechazado por exceder el peso permitido\033[0m")
            peso_equipaje_mano = 0
    else:
        peso_equipaje_mano = 0

    fecha_viaje = input("Ingrese la fecha del viaje (dd/mm/aaaa): ")

    # Generar ID
    id_reserva = generar_id()

    # Calcular costo de equipaje
    costo_equipaje_principal = 0
    for rango, costo in costos_equipaje.items():
        if rango[0] <= peso_equipaje_principal <= rango[1]:
            costo_equipaje_principal = costo
            break

    precio_base = rutas[destino]["precio_base"]
    total = precio_base + costo_equipaje_principal

    # Guardar reserva
    reservas[id_reserva] = {
        "nombre": nombre,
        "tipo_viaje": tipo_viaje,
        "destino": destino,
        "peso_equipaje_principal": peso_equipaje_principal,
        "peso_equipaje_mano": peso_equipaje_mano,
        "fecha_viaje": fecha_viaje,
        "costo_equipaje_principal": costo_equipaje_principal,
        "total": total
    }

    # Mostrar resumen
    print("\033[92m\nReserva registrada con exito.\033[0m")
    print(f"ID de compra: {id_reserva}")
    print(f"Nombre: {nombre}")
    print(f"Destino: {destino}")
    print(f"Fecha del viaje: {fecha_viaje}")
    print(f"Peso equipaje principal: {peso_equipaje_principal} kg")
    print(f"Peso equipaje de mano: {peso_equipaje_mano} kg")
    print(f"Costo total del viaje: ${total:,.2f}")

# Funcion para mostrar todas las reservas
def mostrar_reservas():
    print("\033[34m\n LISTADO DE RESERVAS \033[0m")
    if not reservas:
        print("\033[93mNo hay reservas registradas.\033[0m")
        return
    for id_reserva, reserva in reservas.items():
        print(f"\n\033[96mID: {id_reserva}\033[0m")
        print(f"Nombre: {reserva['nombre']}")
        print(f"Destino: {reserva['destino']}")
        print(f"Fecha: {reserva['fecha_viaje']}")
        print(f"Equipaje principal: {reserva['peso_equipaje_principal']} kg")
        print(f"Equipaje de mano: {reserva['peso_equipaje_mano']} kg")
        print(f"Costo total: ${reserva['total']:,.2f}")

# Funcion para consultar una reserva
def consultar_reserva():
    print("\033[34m\n   CONSULTA DE RESERVA   \033[0m")
    id_reserva = input("Ingrese el ID de compra: ")
    if id_reserva in reservas:
        r = reservas[id_reserva]
        print(f"\n\033[96mID: {id_reserva}\033[0m")
        print(f"Nombre: {r['nombre']}")
        print(f"Destino: {r['destino']}")
        print(f"Fecha: {r['fecha_viaje']}")
        print(f"Equipaje principal: {r['peso_equipaje_principal']} kg")
        print(f"Equipaje de mano: {r['peso_equipaje_mano']} kg")
        print(f"Costo total: ${r['total']:,.2f}")
    else:
        print("\033[91mReserva no encontrada.\033[0m")

# Funcion para mostrar el reporte administrativo
def reporte_admin():
    print("\033[34m\n  REPORTE ADMINISTRATIVO   \033[0m")
    total_recaudado = sum(r['total'] for r in reservas.values())
    print(f"Total recaudado: \033[92m${total_recaudado:,.2f}\033[0m")

    nacionales = 0
    internacionales = 0

    for i in reservas.values():
        if i["tipo_viaje"] == "nacional":
            nacionales += 1
        elif i["tipo_viaje"] == "internacional":
            internacionales += 1

    print("\033[93mNacionales:\033[0m", nacionales)
    print("\033[93mInternacionales:\033[0m", internacionales)

# Menu principal
while True:
    print("\n\033[34m========= MENU PRINCIPAL =========\033[0m")
    print("1. Registrar nueva reserva")
    print("2. Mostrar todas las reservas")
    print("3. Consultar reserva por ID")
    print("4. Reporte administrativo")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        registrar_reserva()
    elif opcion == "2":
        mostrar_reservas()
    elif opcion == "3":
        consultar_reserva()
    elif opcion == "4":
        reporte_admin()
    elif opcion == "5":
        print("\033[91mSaliendo del sistema...\033[0m")
        break
    else:
        print("\033[91mOpcion no valida. Intente nuevamente.\033[0m")