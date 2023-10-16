# Ingreso de variables


lineasdeproduccion = []

# Calculo de ganancia total
def gananciatotal(preciodeventam2, metrosvendidos):
    return preciodeventam2 * metrosvendidos

# Calculo de costo total
def costototal(empleados):
    costototal = 0
    for empleado in empleados:
        numdehorastrabajadas, costohora = empleado
        costototal += numdehorastrabajadas * costohora
    return costototal

# Calculo de ganancia neta
def ganancianeta(gananciatotal, costototal):
    return gananciatotal - costototal

# Calculo del índice de eficiencia
def indicedeeficiencia(ganancianeta, numdeempleados):
    return ganancianeta / numdeempleados

# Solicitar información al usuario
numdelineas = int(input("Ingrese el número de líneas de producción (máximo 4): "))

if numdelineas < 2 or numdelineas >4:
    print("El número de líneas de producción debe estar entre 2 y 4.")
else:
    for linea in range(1, numdelineas + 1):
        print(f"Ingrese información para la Línea de Producción {linea}:")
        preciodeventam2 = float(input("Precio de venta por metro cuadrado: Q"))
        metrosvendidos = float(input("Cantidad de metros cuadrados vendidos al mes: "))
        
        empleados = []
        numdeempleados = 0
        
        while True:
            if numdeempleados >= 20:
                break
            
            try:
                numdehorastrabajadas = float(input(f"Número de horas trabajadas por el empleado {numdeempleados + 1} (0 para finalizar): "))
                if numdehorastrabajadas == 0:
                    break
                costohora = float(input(f"Costo de hora por empleado {numdeempleados + 1}: Q"))
                empleados.append((numdehorastrabajadas, costohora))
                numdeempleados += 1
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos.")

        Gananciatotal = gananciatotal(preciodeventam2, metrosvendidos)
        Costototal = costototal(empleados)
        Ganancianeta = ganancianeta(Gananciatotal, Costototal)
        Indicedeeficiencia = indicedeeficiencia(Ganancianeta, numdeempleados)
        
        lineasdeproduccion.append({
            "Línea": linea,
            "Número de empleados": numdeempleados,
            "Ganancia Total": Gananciatotal,
            "Costo Total": Costototal,
            "Ganancia Neta": Ganancianeta,
            "Índice de Eficiencia": Indicedeeficiencia
        })

    # Comparación de líneas de producción
    lineasdeproduccion.sort(key=lambda x: x["Índice de Eficiencia"], reverse=True)
    mejorlinea = lineasdeproduccion[0]

    # Mostrar resultados
    print("\nResumen de líneas de producción:")
    for linea in lineasdeproduccion:
        print(f"Línea {linea['Línea']}:")
        print(f"- Número de empleados: {linea['Número de empleados']:.2f}")
        print(f"- Ganancia Total: Q{linea['Ganancia Total']:.2f}")
        print(f"- Costo Total: Q{linea['Costo Total']:.2f}")
        print(f"- Ganancia Neta: Q{linea['Ganancia Neta']:.2f}")
        print(f"- Índice de Eficiencia: {linea['Índice de Eficiencia']:.2f}")
        print()

    print(f"La línea de producción más eficiente es la Línea {mejorlinea['Línea']} con un Índice de Eficiencia de {mejorlinea['Índice de Eficiencia']:.2f}.")