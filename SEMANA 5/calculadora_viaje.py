"""
Programa: Calculadora de Costo de Viaje Compartido (Interactivo)
Descripción: Calcula el costo de combustible por persona solicitando datos al usuario.
Utiliza input() para recibir destino, distancia y pasajeros.
Autor: [Tu Nombre Aquí]
Fecha: 2024
"""

def calcular_costo_viaje():
    print("--- BIENVENIDO A LA CALCULADORA DE VIAJES ---")
    
    # --- Entrada de Datos (Interactividad) ---

    # STRING: El usuario ingresa el texto directamente
    destino_viaje = input("¿Cuál es el destino del viaje? ")

    # FLOAT: Convertimos la entrada a decimal para la distancia
    # Nota: El usuario debe usar punto (.) para decimales, ej: 150.5
    distancia_km = float(input(f"¿Cuántos kilómetros hay hasta {destino_viaje}? "))

    # INTEGER: Convertimos la entrada a entero para los pasajeros
    numero_pasajeros = int(input("¿Cuántas personas viajan (incluyendo al conductor)? "))

    # Datos fijos (Constantes para el ejemplo, aunque también podrían pedirse)
    precio_galon = 2.72  # Precio fijo por galón en Ecuador
    consumo_km_por_galon = 45.0

    # --- Lógica del Programa (Cálculos) ---

    # 1. Calcular galones
    galones_necesarios = distancia_km / consumo_km_por_galon

    # 2. Calcular costo total
    costo_total_combustible = galones_necesarios * precio_galon

    # 3. Calcular costo por persona
    costo_por_persona = costo_total_combustible / numero_pasajeros

    # BOOLEAN: Lógica de decisión
    es_viaje_economico = costo_por_persona < 5.00

    # --- Salida de Datos ---
    print("\n" + "="*30) # Línea decorativa
    print(f"--- Resultados para el viaje a {destino_viaje} ---")
    print(f"Distancia: {distancia_km} km")
    print(f"Pasajeros: {numero_pasajeros}")
    print(f"Costo Total Gasolina: ${costo_total_combustible:.2f}")
    print("="*30)
    print(f"COSTO POR PERSONA: ${costo_por_persona:.2f}")
    print(f"¿Es económico (menos de $5)? {es_viaje_economico}")
    print("="*30)
    print("¡Gracias por usar la Calculadora de Viajes!")
    print("Desarrollado por [Jairo Sayay]")

if __name__ == "__main__":
    calcular_costo_viaje()