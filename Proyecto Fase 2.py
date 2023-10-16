# Inicialización de variables y listas
lineasdeproduccion = []
maxdeempleados = 20

# Función para obtener información de una línea de producción
def informacionlinea(numerodelinea):
    print(f"Ingrese la información para la Línea de Producción {numerodelinea}:")
    preciodeventam2 = float(input("Precio de venta por metro cuadrado: Q"))
    metrosvendidos = float(input("Cantidad de metros cuadrados vendidos al mes: "))
    
    empleados = []
    totaldehorastrabajadas = 0

    # Solicitar información de empleados
    while True:
        if len(empleados) >= maxdeempleados:
            break
        try:
            numdehoras = float(input("Número de horas trabajadas por empleado (0 para finalizar): "))
            if numdehoras == 0:
                break
            costoporhora = float(input("Costo de hora por empleado: Q"))
            empleados.append((numdehoras, costoporhora))
            totaldehorastrabajadas += numdehoras
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")
    
    return preciodeventam2, metrosvendidos, empleados, totaldehorastrabajadas

# Función para calcular la ganancia total de una línea de producción
def gananciatotal(preciodeventam2, metrosvendidos):
    return preciodeventam2 * metrosvendidos

# Función para calcular el costo total de una línea de producción
def costototal(empleados):
    return sum(numdehoras * costoporhora for numdehoras, costoporhora in empleados)

# Función para calcular la ganancia neta de una línea de producción
def ganancianeta(gananciatotal, costototal):
    return gananciatotal - costototal

# Función para calcular el índice de eficiencia de una línea de producción
def indiceeficiencia(ganancianeta, numempleados):
    return ganancianeta / numempleados

# Solicitar información de ambas líneas de producción
for linea in range(1, 3):
    precioporm2, metrosvendidos, empleados, horastotales = informacionlinea(linea)
    Gananciatotal = gananciatotal(precioporm2, metrosvendidos)
    Costototal = costototal(empleados)
    Ganancianeta = ganancianeta(Gananciatotal, Costototal)

    if horastotales > 0:
        indicedeeficiencia = indiceeficiencia(Ganancianeta, horastotales)
        lineasdeproduccion.append((linea, Ganancianeta, indicedeeficiencia))
    else:
        print(f"No se ingresó información de empleados para la Línea {linea}.")
    
# Determinar la línea de mayor eficiencia
if lineasdeproduccion:
    lineasdeproduccion.sort(key=lambda x: x[2], reverse=True)
    mejorlinea, mejorganancianeta, mejoreficiencia = lineasdeproduccion[0]
    print("\nResumen de líneas de producción:")
    for linea, Ganancianeta, eficiencia in lineasdeproduccion:
        print(f"Línea {linea}: Ganancia Neta = Q{Ganancianeta:.2f}, Índice de Eficiencia = {eficiencia:.2f}")
    print(f"\nLa línea de producción más eficiente es la Línea {mejorlinea} con una Ganancia Neta de Q{mejorganancianeta:.2f}.")
else:
    print("No se ingresó información válida para ninguna línea de producción.")
