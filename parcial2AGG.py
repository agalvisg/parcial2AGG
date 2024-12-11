def dividir_en_segmentos(numero, tipo):
    """
    Divide un número en segmentos clave según su tipo.
    Tipo 2: toma los caracteres centrales como raíz.
    Tipo 5: toma una sección del medio específica como raíz.
    """
    numero = str(numero)
    if tipo == 2:
        # Segmento para tipo 2: del índice 2 al 6 (ejemplo)
        return [numero[2:7]]
    elif tipo == 5:
        # Segmento para tipo 5: del índice 3 al 7 (ejemplo)
        return [numero[3:7]]
    else:
        raise ValueError("Tipo no soportado.")

def calcular_similitud_segmentos(lista1, lista2):
    """
    Calcula la similitud entre dos listas de segmentos clave.
    """
    coincidencias = 0
    for seg1, seg2 in zip(lista1, lista2):
        if seg1 == seg2:
            coincidencias += 1
    return coincidencias / len(lista1)

def clasificar_identificador(lista_original, numero_objetivo, tipo, umbral=0.8):
    """
    Clasifica el número objetivo como "similar" o "nuevo"
    comparando sus segmentos clave.
    """
    numero_mas_parecido = None
    mayor_similitud = 0
    segmentos_objetivo = dividir_en_segmentos(numero_objetivo, tipo)

    for num in lista_original:
        segmentos_actual = dividir_en_segmentos(num, tipo)
        similitud = calcular_similitud_segmentos(segmentos_objetivo, segmentos_actual)
        if similitud > mayor_similitud:
            mayor_similitud = similitud
            numero_mas_parecido = num

    # Verificar si la similitud supera el umbral
    if mayor_similitud >= umbral:
        return numero_mas_parecido
    else:
        return "nuevo"

# Lista original (ya no la procesamos con split)
lista_original = [2441006710, 5581023627]

# Seleccionar el tipo de identificador
tipo = int(input("Ingresa el tipo de identificador (2 o 5): "))

# Umbral de similitud
umbral = float(input("Ingresa el umbral de similitud (valor entre 0 y 1, por defecto 0.8): ") or 0.8)

# Análisis de números objetivo
print("\nEscribe los números a analizar. Escribe 'salir' para terminar.")
while True:
    entrada = input("Número a analizar: ")
    if entrada.lower() == "salir":
        break
    try:
        numero_objetivo = int(entrada)
        resultado = clasificar_identificador(lista_original, numero_objetivo, tipo, umbral)
        print(f"El número {numero_objetivo} se clasifica como: {resultado}")
    except ValueError:
        print("Por favor, ingresa un número válido o 'salir' para terminar.")
