from Inputs import pedir_opcion_menu

# Pide al usuario un nombre válido (mínimo 3 letras, solo letras y espacios)
def pedir_nombre():
    while True:
        nombre = input("Nombre del participante: ")
        if len(nombre) >= 3:
            letras_validas = True
            for letra in nombre:
                es_letra = (letra >= "a" and letra <= "z") or (letra >= "A" and letra <= "Z")
                if not (es_letra or letra == " "):
                    letras_validas = False
            if letras_validas:
                return nombre
            else:
                print("ERROR: Solo letras y espacios.")
        else:
            print("ERROR: Mínimo 3 letras.")

# Pide al usuario una puntuación del jurado (entre 1 y 10)
def pedir_puntaje(numero_jurado):
    while True:
        texto = input("Puntaje jurado " + str(numero_jurado) + ": ")
        try:
            numero = int(texto)
            if 1 <= numero <= 10:
                return numero
            else:
                print("ERROR: Entre 1 y 10.")
        except:
            print("ERROR: Solo números.")

# Crea una lista de 5 participantes vacíos (con nombre, puntajes y promedio)
def cargar_participantes():
    lista_participantes = [None] * 5
    for posicion in range(5):
        print("\nParticipante", posicion + 1)
        nombre = pedir_nombre()
        lista_participantes[posicion] = [nombre, [], 0.0]
    return lista_participantes

# Carga los puntajes de 3 jurados para cada participante y calcula su promedio
def cargar_puntajes(lista_participantes):
    for indice_participante in range(5):
        nombre = lista_participantes[indice_participante][0]
        print("\nPuntajes de", nombre)
        puntaje_1 = pedir_puntaje(1)
        puntaje_2 = pedir_puntaje(2)
        puntaje_3 = pedir_puntaje(3)
        lista_participantes[indice_participante][1] = [puntaje_1, puntaje_2, puntaje_3]
        lista_participantes[indice_participante][2] = (puntaje_1 + puntaje_2 + puntaje_3) / 3

# Muestra el nombre, puntajes y promedio de cada participante
def mostrar_puntajes(lista_participantes):
    for participante in lista_participantes:
        nombre = participante[0]
        puntajes = participante[1]
        promedio = participante[2]
        print(nombre, "->", puntajes, "-> Promedio:", "%.2f" % promedio)

# Muestra los participantes que tienen un promedio mayor al mínimo indicado
def mostrar_promedios_mayores(lista_participantes, minimo):
    hay_resultados = False
    for participante in lista_participantes:
        nombre = participante[0]
        promedio = participante[2]
        if promedio > minimo:
            print(nombre, "->", "%.2f" % promedio)
            hay_resultados = True
    if not hay_resultados:
        print("ERROR: Nadie supera ese promedio.")

# Calcula y muestra el promedio de cada jurado en base a todos los participantes
def promedio_por_jurado(lista_participantes):
    suma_jurados = [0, 0, 0]
    for participante in lista_participantes:
        puntajes = participante[1]
        for numero_de_jurado in range(3):
            suma_jurados[numero_de_jurado] += puntajes[numero_de_jurado]
    for numero_de_jurado in range(3):
        promedio = suma_jurados[numero_de_jurado] / 5
        print("Jurado", numero_de_jurado + 1, "->", "%.2f" % promedio)

# Muestra cual jurado dio los puntajes más bajos en promedio
def jurado_estricto(lista_participantes):
    suma_jurados = [0, 0, 0]
    for participante in lista_participantes:
        puntajes = participante[1]
        for numero_de_jurado in range(3):
            suma_jurados[numero_de_jurado] += puntajes[numero_de_jurado]
    promedios = [suma / 5 for suma in suma_jurados]
    promedio_mas_bajo = min(promedios)
    for numero_de_jurado in range(3):
        if promedios[numero_de_jurado] == promedio_mas_bajo:
            print("EL Jurado N°", numero_de_jurado + 1, "es el mas estricto.")

# Permite buscar un participante por nombre hasta que se encuentre
def buscar_participante(lista_participantes):
    encontrado = False
    while encontrado == False:
        nombre_buscado = input("Buscar nombre: ").lower()
        for participante in lista_participantes:
            nombre = participante[0]
            if nombre.lower() == nombre_buscado:
                puntajes = participante[1]
                promedio = participante[2]
                print(nombre, "->", puntajes, "-> Promedio:", "%.2f" % promedio)
                encontrado = True
                break
        if encontrado == False:
            print("ERROR: El nombre que buscas NO conicide con los datos ingresados.")

# Muestra los 3 participantes con mayor promedio
def top3(lista_participantes):
    copia = lista_participantes[:]
    for posicion_actual in range(5):
        for siguiente_posicion in range(posicion_actual + 1, 5):
            if copia[siguiente_posicion][2] > copia[posicion_actual][2]:
                copia[posicion_actual], copia[siguiente_posicion] = copia[siguiente_posicion], copia[posicion_actual]
    for lugar in range(3):
        nombre = copia[lugar][0]
        promedio = copia[lugar][2]
        print(nombre, "->", "%.2f" % promedio)

# Ordena y muestra los participantes por nombre (A-Z)
def ordenar_alfabetico(lista_participantes):
    copia = lista_participantes[:]
    for posicion_actual in range(5):
        for siguiente_posicion in range(posicion_actual + 1, 5):
            if copia[siguiente_posicion][0].lower() < copia[posicion_actual][0].lower():
                copia[posicion_actual], copia[siguiente_posicion] = copia[siguiente_posicion], copia[posicion_actual]
    for participante in copia:
        nombre = participante[0]
        promedio = participante[2]
        print(nombre, "-> Promedio:", "%.2f" % promedio)